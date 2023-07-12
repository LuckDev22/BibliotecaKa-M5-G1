from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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
    email = models.EmailField(max_length=127, unique=True)
    date_birth = models.DateField()
    cpf = models.IntegerField(
        unique=True,
    )
    category_preference = models.CharField(
        max_length=60, choices=CategoryChoices.choices, default=CategoryChoices.OUTROS
    )
    is_student = models.BooleanField(null=True, default=False)
    is_blocked = models.BooleanField(default=False)
    blocked_until = models.DateField(default=None, null=True)

    def get_blocked_status(self):
        if self.is_blocked:
            if self.blocked_until is not None:
             if self.blocked_until <= timezone.now().date():
                return "Bloqueado até " + str(self.blocked_until)
            else:
                return "Bloqueado"
        else:
            return "Bloqueado"
        return "Bloqueado até " + str(self.blocked_until)
