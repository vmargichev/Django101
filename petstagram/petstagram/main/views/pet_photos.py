from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from oauthlib.openid.connect.core.exceptions import LoginRequired

from petstagram.main.forms import CreatePetPhotoForm, EditPetPhotoForm
from petstagram.main.models import PetPhoto

def pet_photo_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
            'form': form,
            'object': instance,
        }
    return render(request, template_name, context)

def show_pet_photo_details(request, pk):
    pet_photo = get_object_or_404(PetPhoto, pk=pk)

    context = {
        'pet_photo': pet_photo
    }
    return render(request, 'photo_details.html', context)

class PetPhotoDetailsView(LoginRequiredMixin, DetailView):
    model = PetPhoto
    template_name = 'photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context

def like_pet_photo(request, pk):
    pet_photo = get_object_or_404(PetPhoto, pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)

class CreatePetPhotoView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    form_class = CreatePetPhotoForm
    template_name = 'photo_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPetPhotoView(LoginRequiredMixin, UpdateView):
    model = PetPhoto
    form_class = EditPetPhotoForm
    template_name = 'photo_edit.html'
    # success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.pk})


def create_pet_photo(request):
    return pet_photo_action(request, CreatePetPhotoForm, 'dashboard', PetPhoto(), 'photo_create.html')
