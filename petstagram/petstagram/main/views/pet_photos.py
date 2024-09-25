from django.shortcuts import get_object_or_404, redirect, render

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

def like_pet_photo(request, pk):
    pet_photo = get_object_or_404(PetPhoto, pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)

def create_pet_photo(request):
    return pet_photo_action(request, CreatePetPhotoForm, 'dashboard', PetPhoto(), 'photo_create.html')

def edit_pet_photo(request, pk):
    return pet_photo_action(request, EditPetPhotoForm, 'dashboard', get_object_or_404(PetPhoto, pk=pk), 'photo_edit.html')