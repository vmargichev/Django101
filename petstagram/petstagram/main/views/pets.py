from django.shortcuts import redirect, render

from petstagram.main.forms import CreatePetForm, DeletePetForm, EditPetForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import Pet

def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        # else:
        #     # If form is invalid, we still need to render the form with errors
        #     context = {
        #         'form': form,
        #         'pet': instance,
        #     }
        #     return render(request, template_name, context)
    else:
        form = form_class(instance=instance)
        
    context = {
            'form': form,
            'pet': instance,
        }
    return render(request, template_name, context)

def create_pet(request):
    return pet_action(request, CreatePetForm, 'profile details', Pet(user_profile=get_profile()), 'pet_create.html')

def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile details', Pet.objects.get(pk=pk), 'pet_edit.html')

def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile details', Pet.objects.get(pk=pk), 'pet_delete.html')