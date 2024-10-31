from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from petstagram.common.validators import file_max_size_validator

UserModel = get_user_model()

# Create your models here.


class Pet(models.Model):

    NAME_MAX_LENGTH =30

    DOG = 'Dog'
    CAT = 'Cat'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (DOG, CAT, BUNNY, PARROT, FISH, OTHER)] 

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        # unique=True,
    )
    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=TYPES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.now().year - self.date_of_birth.year


    def __str__(self) -> str:
        return f'{self.name} {self.type}'

    class Meta():
        unique_together = ('user', 'name')
    
class PetPhoto(models.Model):

    photo = models.ImageField(
        validators= (
            file_max_size_validator,
        ),
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        #validate at least 1 pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
