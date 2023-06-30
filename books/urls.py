from django.urls import path

from views import BooksView
from books import views as song_views

urlpatterns = [
    path("books/", BooksView.as_view()),
]
