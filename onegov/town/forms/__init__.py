from onegov.town.forms.allocation import (
    DaypassAllocationForm,
    RoomAllocationForm
)
from onegov.town.forms.form_definition import (
    BuiltinDefinitionForm,
    CustomDefinitionForm
)
from onegov.town.forms.page import LinkForm, PageForm
from onegov.town.forms.person import PersonForm
from onegov.town.forms.reset_password import (
    RequestPasswordResetForm,
    PasswordResetForm
)
from onegov.town.forms.resource import ResourceForm
from onegov.town.forms.settings import SettingsForm

__all__ = [
    'BuiltinDefinitionForm',
    'CustomDefinitionForm',
    'DaypassAllocationForm',
    'LinkForm',
    'PageForm',
    'PasswordResetForm',
    'PersonForm',
    'ResourceForm',
    'RequestPasswordResetForm',
    'RoomAllocationForm',
    'SettingsForm',
]