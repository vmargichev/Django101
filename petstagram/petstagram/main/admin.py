from django.contrib import admin

from petstagram.main.models import Pet, PetPhoto

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=('name', 'type')

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass