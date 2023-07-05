from rest_framework.generics import ListCreateAPIView
from .serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from .models import Loan
from books.models import Book
from users.models import User
from django.views import View
from django.http import HttpResponse
from datetime import datetime, timedelta


class LoanView(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book)


class CreateLoanView(View):
    def post(self, request):
        user_id = request.POST.get("user_id")
        book_id = request.POST.get("book_id")

        book = get_object_or_404(Book, id=book_id)
        if not book.is_available():
            return HttpResponse("Livro não disponível para empréstimo.")

        user = get_object_or_404(User, id=user_id)
        if user.is_blocked:
            return HttpResponse("Usuário bloqueado para empréstimos.")

        current_date = datetime.now().date()
        return_due_date = current_date + timedelta(days=5)

        loan = Loan.objects.create(
            user_id=user_id, book_id=book_id, return_due_date=return_due_date
        )

        book.is_borrowed = True
        book.save()

        user.is_blocked = True
        user.save()

        return HttpResponse("Empréstimo realizado com sucesso.")


class ReturnLoanView(View):
    def post(self, request):
        loan_id = request.POST.get("loan_id")

        loan = get_object_or_404(Loan, id=loan_id)

        loan.is_returned = True
        loan.save()

        user = loan.user
        pending_loans = Loan.objects.filter(user=user, is_returned=False).exists()
        if not pending_loans:
            user.is_blocked = False
            user.save()

        return HttpResponse("Empréstimo devolvido com sucesso.")
