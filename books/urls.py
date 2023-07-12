from django.urls import path
from .views import BooksView
from copies.views import CopyView

urlpatterns = [
    path("books/", BooksView.as_view()),
    path("books/<int:pk>/copies/", CopyView.as_view()),
]
