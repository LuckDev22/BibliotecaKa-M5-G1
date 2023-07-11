from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=25)
    publishing_company = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    user = models.ManyToManyField("users.User", related_name="books")

