from django.views.generic import RedirectView

from petstagram.accounts.views import UserLoginView, UserRegisterView, UserEditProfileView, UserDeleteView, \
    UserChangePasswordView
from django.urls import path, reverse_lazy

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),

    path('edit-password/', UserChangePasswordView.as_view(), name='change password'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/<int:pk>/', UserEditProfileView.as_view(), name='edit profile'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete profile'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
)