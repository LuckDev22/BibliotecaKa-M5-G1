from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
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
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
