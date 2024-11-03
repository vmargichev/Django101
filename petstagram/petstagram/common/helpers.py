import os

from petstagram.accounts.models import Profile

class BootstrapMixin:
    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'

class DisableFieldsFormMixin:
    # disabled_fields = '__all__'

    def _init_disabled_fields(self, disabled_fields):

        for name, field in self.fields.items():
            if disabled_fields != '__all__' and name not in disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['disabled'] = True

def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def is_production():
    if os.getenv('APP_ENVIRONMENT') == 'Production':
        return True