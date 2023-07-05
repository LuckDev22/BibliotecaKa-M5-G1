from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from datetime import timedelta, datetime
from pytz import timezone
from .serializers import LoanSerializer

from .models import Loan
from books.models import Book
from users.models import User
from copies.models import Copy


class LoanView(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        copy_status = self.request.data.get("status", "Disponível")
        copies_numbers = self.request.data.get("copies_numbers", 1)
        user_id = self.request.data.get("user_id")
        if user_id is None:
            raise ValueError("ID do usuário é obrigatório.")
        user = get_object_or_404(User, pk=user_id)
        copy = Copy(book=book, status=copy_status, copies_numbers=copies_numbers)
        copy.save()
        loan = serializer.save(copy=copy, user=user)
        self.adjust_return_date(loan)  # Ajuste da data de devolução
        loan.save()

    def adjust_return_date(self, loan):
        if loan.data_devolucao.weekday() >= 5:  # 5 e 6 representam sábado e domingo
            loan.data_devolucao += timedelta(days=7 - loan.data_devolucao.weekday())
        loan.save()
