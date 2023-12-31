from rest_framework import serializers
from copies.serializers import CopySerializer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    copies = CopySerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication_date",
            "author",
            "category",
            "publishing_company",
            "description",
            "copies",
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
