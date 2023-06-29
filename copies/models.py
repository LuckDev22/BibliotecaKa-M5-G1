from django.db import models


# Create your models here.
class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    estado_choices = [
        ("disponivel", "Disponível"),
        ("emprestada", "Emprestada"),
        ("danificada", "Danificada"),
        ("perdida", "Perdida"),
    ]
    estado = models.CharField(max_length=20, choices=estado_choices)
    livro = models.ForeignKey("books.Book", on_delete=models.CASCADE)
