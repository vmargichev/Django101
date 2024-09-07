from django.contrib import admin

from petstagram.main.models import Profile, Pet, PetPhoto

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name')

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=('name', 'type')

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass