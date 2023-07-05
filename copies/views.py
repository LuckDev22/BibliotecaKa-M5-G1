from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Copy
from books.models import Book
from .serializers import CopySerializer


class CopyView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book_id = self.request.data.get("book_id")
        try:
            book = Book.objects.get(id=book_id)
            serializer.save(book=book)
        except Book.DoesNotExist:
            return Response(
                {"error": "O livro especificado não existe."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CopyDetailView(generics.RetrieveAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
