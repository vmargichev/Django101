from datetime import datetime
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main.validators import file_max_size_validator, only_letters_validator

# Create your models here.
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

    description = models.TextField(
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
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

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

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    @property
    def age(self):
        return datetime.now().year - self.date_of_birth.year


    def __str__(self) -> str:
        return f'{self.name} {self.type}'

    class Meta():
        unique_together = ('user_profile', 'name')
    
class PetPhoto(models.Model):

    photo = models.ImageField(
        validators= (
            file_max_size_validator,
        )
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
