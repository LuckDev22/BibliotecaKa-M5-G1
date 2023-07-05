from django.urls import path
from .views import BooksView, LoanView

urlpatterns = [
    path("books/", BooksView.as_view()),
    path("books/<int:pk>/loans/", LoanView.as_view()),
]
