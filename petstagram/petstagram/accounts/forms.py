from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from petstagram.common.helpers import BootstrapMixin
from petstagram.accounts.models import Profile
from django import forms

from petstagram.main.models import PetPhoto


class CreateProfileForm(BootstrapMixin, UserCreationForm):

    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LENGTH,)
    last_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LENGTH,)
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDERS,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user = user)

        if commit:
            profile.save()

        return user

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'picture',
            'description',
        )

        widgets = {
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

        widgets = {
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
        #Not good should be done with signals
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'email', 'date_of_birth', 'description', 'picture', 'gender')