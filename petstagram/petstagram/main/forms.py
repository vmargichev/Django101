from datetime import date
from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from petstagram.main.helpers import BootstrapMixin, DisableFieldsFormMixin
from petstagram.main.models import Pet, PetPhoto, Profile

class CreateProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'picture',   
        )
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }

class EditProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'

        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter Email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            ),
        
        }

class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        pets = self.instance.pet_set.all()
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance
    
    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'email', 'date_of_birth', 'description', 'picture', 'gender')

class CreatePetForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }

class EditPetForm(BootstrapMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        
        if date_of_birth < self.MIN_DATE_OF_BIRTH or self.MAX_DATE_OF_BIRTH < date_of_birth:
                raise ValidationError( f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}')
        
        return date_of_birth
    
    class Meta:
        model = Pet
        exclude = ('user_profile',)

class DeletePetForm(BootstrapMixin, DisableFieldsFormMixin, forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields('__all__')

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
    
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth',)
        # widgets = {
        #     'name': forms.TextInput(attrs={'disabled': True}),
        #     'type': forms.Select(attrs={'disabled': True}),
        #     'date_of_birth': forms.DateInput(attrs={'disabled': True}),
        # }
class CreatePetPhotoForm(BootstrapMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
    
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        widgets={
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),
        }

class EditPetPhotoForm(BootstrapMixin, DisableFieldsFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields('photo')
    
    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        widgets={
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),
        }
        