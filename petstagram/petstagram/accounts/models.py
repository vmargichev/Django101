from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.accounts.managers import PetstagramManager
from petstagram.common.validators import only_letters_validator

# Create your models here.
'''
Create model extending
Configure this model in settings.py
create user manager
'''


class PetstagramUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramManager()

class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH =30
    FIRST_NAME_MIN_LENGTH =2
    LAST_NAME_MAX_LENGTH =30
    LAST_NAME_MIN_LENGTH =2

    MALE='MALE'
    FEMALE='FEMALE'
    DO_NOT_SHOW='Do not Show'

    GENDERS=[(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    #id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators = (
            MinLengthValidator(
                limit_value=FIRST_NAME_MIN_LENGTH,
                               ),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
