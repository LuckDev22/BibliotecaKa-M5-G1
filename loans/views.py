from rest_framework.generics import ListCreateAPIView
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from .models import Loan
from books.models import Book


class LoanView(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book)
