from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    # tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    # historico_emprestimos = models.ManyToManyField(Emprestimo)
