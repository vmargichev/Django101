from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from petstagram.accounts.forms import CreateProfileForm
from petstagram.accounts.models import Profile
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from petstagram.common.view_mixins import RedirectToDashboardIfLoggedInMixin
from petstagram.main.models import Pet, PetPhoto

# Create your views here.
class UserRegisterView(SuccessMessageMixin, RedirectToDashboardIfLoggedInMixin, CreateView):
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')
    template_name = 'create_profile.html'

class UserLoginView(auth_views.LoginView):
    template_name = 'login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

class UserProfileView(View):
    pass

class UserEditProfileView(View):
    pass

class UserChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('dashboard')
    template_name = 'change_pass.html'
    pass


class UserDeleteView(View):
    pass

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        total_pet_photos_count = len(pet_photos)
        total_likes_count = sum(pp.likes for pp in pet_photos)

        context.update({
            'total_pet_photos_count': total_pet_photos_count,
            'total_likes_count': total_likes_count,
            'is_owner': self.object.user_id == self.request.user.pk,
            'pets': pets,
        })

        return context
