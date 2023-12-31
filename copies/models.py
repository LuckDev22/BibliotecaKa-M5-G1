from django.db import models


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    status_choices = [
        ("disponivel", "Disponível"),
        ("emprestada", "Emprestada"),
        ("danificada", "Danificada"),
        ("perdida", "Perdida"),
    ]

    status = models.CharField(max_length=20, choices=status_choices)
    copies_numbers = models.IntegerField(default=1)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
