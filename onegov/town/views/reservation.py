import morepath

from libres.db.models import Allocation, Reservation
from libres.modules.errors import LibresError
from onegov.core.security import Public, Private
from onegov.form import FormCollection
from onegov.libres import ResourceCollection
from onegov.ticket import TicketCollection
from onegov.town import TownApp, _, utils
from onegov.town.elements import Link
from onegov.town.forms import ReservationForm
from onegov.town.layout import ReservationLayout
from onegov.town.mail import send_html_mail
from sqlalchemy.orm.attributes import flag_modified
from purl import URL
from uuid import uuid4
from webob import exc


def get_reservation_form_class(model, request):
    if isinstance(model, Allocation):
        return ReservationForm.for_allocation(model)

    if isinstance(model, Reservation):
        allocation = model._target_allocations().first()
        return ReservationForm.for_allocation(allocation)

    raise NotImplementedError


def get_libres_session_id(request):
    if not request.browser_session.has('libres_session_id'):
        request.browser_session.libres_session_id = uuid4()

    return request.browser_session.libres_session_id


def get_submission_link(request, submission, confirm_link):
    url = URL(request.link(submission))
    url = url.query_param('return-to', confirm_link)
    url = url.query_param('title', request.translate(
        _("Details about the reservation"))
    )
    url = url.query_param('edit', 1)
    url = url.query_param('quiet', 1)

    return url.as_string()


@TownApp.form(model=Allocation, name='reservieren', template='reservation.pt',
              permission=Public, form=get_reservation_form_class)
def handle_reserve_allocation(self, request, form):
    """ Creates a new reservation for the given allocation.
    """

    collection = ResourceCollection(request.app.libres_context)
    resource = collection.by_id(self.resource)

    if form.submitted(request):
        start, end = form.get_date_range()

        try:
            scheduler = resource.get_scheduler(request.app.libres_context)
            token = scheduler.reserve(
                email=form.data['email'],
                dates=(start, end),
                quota=int(form.data.get('quota', 1)),
                session_id=get_libres_session_id(request)
            )
        except LibresError as e:
            utils.show_libres_error(e, request)
        else:
            # while we re at it, remove all expired sessions
            resource.remove_expired_reservation_sessions(
                request.app.libres_context)

            # though it's possible for a token to have multiple reservations,
            # it is not something that can happen here -> therefore one!
            reservation = scheduler.reservations_by_token(token).one()
            confirm_link = request.link(reservation, 'bestaetigung')

            if not resource.definition:
                return morepath.redirect(confirm_link)

            # if extra form data is required, this is the first step.
            # together with the unconfirmed, session-bound reservation,
            # we create a new external submission without any data in it.
            # the user is then redirected to the reservation data edit form
            # where the reservation is finalized and a ticket is opened.
            forms = FormCollection(request.app.session())
            submission = forms.submissions.add_external(
                form=resource.form_class(),
                state='pending',
                id=reservation.token
            )

            return morepath.redirect(
                get_submission_link(request, submission, confirm_link)
            )

    layout = ReservationLayout(resource, request)
    layout.breadcrumbs.append(Link(_("Reserve"), '#'))

    title = _("New reservation for ${title}", mapping={
        'title': resource.title,
    })

    return {
        'layout': layout,
        'title': title,
        'form': form,
        'allocation': self,
        'button_text': _("Continue")
    }


@TownApp.form(model=Reservation, name='bearbeiten', template='reservation.pt',
              permission=Public, form=get_reservation_form_class)
def handle_edit_reservation(self, request, form):

    # this view is public, but only for a limited time
    assert_anonymous_access_only_temporary(self, request)

    collection = ResourceCollection(request.app.libres_context)
    resource = collection.by_id(self.resource)

    if form.submitted(request):
        scheduler = resource.get_scheduler(request.app.libres_context)
        try:
            if self.email != form.email.data:
                scheduler.change_email(self.token, form.email.data)

            start, end = form.get_date_range()
            scheduler.change_reservation(
                self.token, self.id, start, end, quota=form.data.get('quota')
            )
        except LibresError as e:
            utils.show_libres_error(e, request)
        else:
            forms = FormCollection(request.app.session())
            submission = forms.submissions.by_id(self.token)
            confirm_link = request.link(self, 'bestaetigung')

            if submission is None:
                return morepath.redirect(confirm_link)
            else:
                return morepath.redirect(
                    get_submission_link(request, submission, confirm_link)
                )

    form.apply_model(self)

    layout = ReservationLayout(resource, request)
    layout.breadcrumbs.append(Link(_("Edit Reservation"), '#'))

    title = _("Change reservation for ${title}", mapping={
        'title': resource.title,
    })

    return {
        'layout': layout,
        'title': title,
        'form': form,
        'allocation': self,
        'button_text': _("Continue")
    }


def assert_anonymous_access_only_temporary(self, request):
    """ Raises exceptions if the current user is anonymous and no longer
    should be given access to the reservation models.

    This could probably be done using morepath's security system, but it would
    not be quite as straight-forward. This approach is, though we have
    to manually add this function to all reservation views the anonymous user
    should be able to access when creating a new reservatin, but not anymore
    after that.

    """
    if request.is_logged_in:
        return

    if not self.session_id:
        raise exc.HTTPForbidden()

    if self.status == 'approved':
        raise exc.HTTPForbidden()

    if self.session_id != get_libres_session_id(request):
        raise exc.HTTPForbidden()


@TownApp.html(model=Reservation, name='bestaetigung', permission=Public,
              template='reservation_confirmation.pt')
def confirm_reservation(self, request):

    # this view is public, but only for a limited time
    assert_anonymous_access_only_temporary(self, request)

    collection = ResourceCollection(request.app.libres_context)
    resource = collection.by_id(self.resource)

    forms = FormCollection(request.app.session())
    submission = forms.submissions.by_id(self.token)

    if submission:
        form = request.get_form(submission.form_class, data=submission.data)
    else:
        form = None

    layout = ReservationLayout(resource, request)
    layout.breadcrumbs.append(Link(_("Confirm"), '#'))

    return {
        'title': _("Confirm your reservation"),
        'layout': layout,
        'form': form,
        'resource': resource,
        'allocation': self._target_allocations().first(),
        'reservation': self,
        'finalize_link': request.link(self, 'abschluss'),
        'edit_link': request.link(self, 'bearbeiten')
    }


@TownApp.html(model=Reservation, name='abschluss', permission=Public,
              template='layout.pt')
def finalize_reservation(self, request):

    # this view is public, but only for a limited time
    assert_anonymous_access_only_temporary(self, request)

    collection = ResourceCollection(request.app.libres_context)
    resource = collection.by_id(self.resource)
    scheduler = resource.get_scheduler(request.app.libres_context)
    session_id = get_libres_session_id(request)

    try:
        scheduler.queries.confirm_reservations_for_session(session_id)
        scheduler.approve_reservations(self.token)
    except LibresError as e:
        utils.show_libres_error(e, request)

        layout = ReservationLayout(resource, request)
        layout.breadcrumbs.append(Link(_("Error"), '#'))

        return {
            'title': _("The reservation could not be completed"),
            'layout': layout,
        }
    else:
        forms = FormCollection(request.app.session())
        submission = forms.submissions.by_id(self.token)

        if submission:
            forms.submissions.complete_submission(submission)

        with forms.session.no_autoflush:
            ticket = TicketCollection(request.app.session()).open_ticket(
                handler_code='RSV', handler_id=self.token.hex
            )

        send_html_mail(
            request=request,
            template='mail_ticket_opened.pt',
            subject=_("A ticket has been opened"),
            receivers=(self.email, ),
            content={
                'model': ticket
            }
        )

        request.success(_("Thank you for your reservation!"))
        request.app.update_ticket_count()

        return morepath.redirect(request.link(ticket, 'status'))


@TownApp.view(model=Reservation, name='annehmen', permission=Private)
def accept_reservation(self, request):
    if not self.data or not self.data.get('accepted'):
        collection = ResourceCollection(request.app.libres_context)
        resource = collection.by_id(self.resource)
        scheduler = resource.get_scheduler(request.app.libres_context)
        reservations = scheduler.reservations_by_token(self.token)

        send_html_mail(
            request=request,
            template='mail_reservation_accepted.pt',
            subject=_("Your reservation was accepted"),
            receivers=(self.email, ),
            content={
                'model': self,
                'resource': resource,
                'reservations': reservations
            }
        )

        for reservation in reservations:
            reservation.data = reservation.data or {}
            reservation.data['accepted'] = True

            # libres does not automatically detect changes yet
            flag_modified(reservation, 'data')

        request.success(_("The reservation was accepted"))
    else:
        request.warning(_("The reservation has already been accepted"))

    return morepath.redirect(request.params['return-to'])


@TownApp.view(model=Reservation, name='absagen', permission=Private)
def reject_reservation(self, request):
    collection = ResourceCollection(request.app.libres_context)
    resource = collection.by_id(self.resource)
    scheduler = resource.get_scheduler(request.app.libres_context)
    reservations = scheduler.reservations_by_token(self.token.hex)
    forms = FormCollection(request.app.session())
    submission = forms.submissions.by_id(self.token.hex)

    send_html_mail(
        request=request,
        template='mail_reservation_rejected.pt',
        subject=_("Your reservation was rejected"),
        receivers=(self.email, ),
        content={
            'model': self,
            'resource': resource,
            'reservations': reservations
        }
    )

    # create a snapshot of the ticket to keep the useful information
    tickets = TicketCollection(request.app.session())
    ticket = tickets.by_handler_id(self.token.hex)
    ticket.create_snapshot(request)

    scheduler.remove_reservation(self.token.hex)

    if submission:
        forms.submissions.delete(submission)

    request.success(_("The reservation was rejected"))

    # return none on intercooler js requests
    if not request.headers.get('X-IC-Request'):
        return morepath.redirect(request.params['return-to'])
