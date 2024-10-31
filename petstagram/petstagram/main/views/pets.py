from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from petstagram.main.forms import CreatePetForm, DeletePetForm, EditPetForm
from petstagram.main.models import Pet

class CreatePetView(CreateView):
    form_class = CreatePetForm
    template_name = 'pet_create.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Pet'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class DeletePetView(DeleteView):
    model = Pet
    form_class = DeletePetForm
    template_name = 'pet_delete.html'

class EditPetView(UpdateView):
    model = Pet
    form_class = EditPetForm
    template_name = 'pet_edit.html'
