from onegov.core.utils import sanitize_html
from onegov.form import Form, with_options
from onegov.form.validators import ValidFormDefinition
from onegov.town import _
from onegov.town.utils import mark_images
from wtforms import StringField, TextAreaField, validators
from wtforms.widgets import TextArea


class ResourceForm(Form):
    """ Defines the form for all resources. """
    title = StringField(_("Title"), [validators.InputRequired()])

    lead = TextAreaField(
        label=_("Lead"),
        description=_("Describes what this reservation resource is about"),
        widget=with_options(TextArea, rows=4))

    text = TextAreaField(
        label=_("Text"),
        widget=with_options(TextArea, class_='editor'),
        filters=[sanitize_html, mark_images])

    definition = TextAreaField(
        label=_(u"Form Definition"),
        validators=[validators.Optional(), ValidFormDefinition()],
        widget=with_options(TextArea, rows=32, **{'data-editor': 'form'}),
    )

    def update_model(self, model):
        """ Stores the form values on the page. """
        model.title = self.title.data
        model.meta = {
            'lead': self.lead.data
        }
        model.content = {
            'text': self.text.data
        }
        model.definition = self.definition.data

    def apply_model(self, model):
        """ Stores the page values on the form. """
        self.title.data = model.title
        self.lead.data = model.meta.get('lead', '')
        self.text.data = model.content.get('text', '')
        self.definition.data = model.definition or ""
