from django.urls import path

from petstagram.main.views.generic import DashboardPageView, HomePageView
from petstagram.main.views.pet_photos import create_pet_photo, like_pet_photo, show_pet_photo_details, \
    CreatePetPhotoView, PetPhotoDetailsView, EditPetPhotoView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.accounts.views import ProfileDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),

    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile details'),
    # path('profile/create/', create_profile, name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='create pet photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pet/create/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
]


