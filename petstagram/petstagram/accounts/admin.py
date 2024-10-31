from django.contrib import admin
import petstagram.accounts.models as models

# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name')
