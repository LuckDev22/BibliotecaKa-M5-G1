from django.urls import path

from .views import BooksView
from copies import views as copy_views

urlpatterns = [
    path("books/", BooksView.as_view()),
    path("books/<int:pk>/copies/", copy_views.CopyView.as_view())
]
