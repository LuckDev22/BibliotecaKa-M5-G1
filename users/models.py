from django.db import models
from django.contrib.auth.models import AbstractUser


class CategoryChoices(models.TextChoices):
    TERROR = "Terror"
    COMEDIA = "Comedia"
    SUSPENSE = "Suspense"
    ROMANCE = "Romance"
    FANTASIA = "Fantasia"
    OUTROS = "Outros"


class User(AbstractUser):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    date_birth = models.DateField()
    cpf = models.IntegerField(max_length=11, unique=True)
    category_preference = models.CharField(
        choices=CategoryChoices.choices, default=CategoryChoices.choices.OUTROS
    )
    is_student = models.BooleanField(null=True, default=False)
