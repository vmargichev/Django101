from django.shortcuts import get_object_or_404, redirect, render

from petstagram.main.templatetags.profiles import has_profile
from petstagram.main.models import PetPhoto, Profile

# Create your views here.
def get_profiles():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    context = {
        'hide_additional_nav_items': True,
    }

    return render(request, 'home_page.html', context)

def show_dashboard(request):

    profile = get_profiles()
    pet_photos = set(PetPhoto.objects \
        .filter(tagged_pets__user_profile=profile))
    
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)

def show_profile(request):
    return render(request, 'profile_details.html')

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