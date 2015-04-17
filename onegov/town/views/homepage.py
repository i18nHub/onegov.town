""" The onegov town homepage. """

from onegov.core.security import Public
from onegov.town import _
from onegov.town.app import TownApp
from onegov.town.model import Town
from onegov.town.layout import DefaultLayout


@TownApp.html(model=Town, template='town.pt', permission=Public)
def view_town(self, request):
    """ Renders the town's homepage. """
    return {
        'layout': DefaultLayout(self, request),
        'title': _(u'Welcome to ${town}', mapping={'town': self.name})
    }