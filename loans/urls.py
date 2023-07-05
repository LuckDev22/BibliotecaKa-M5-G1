from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("loans/", views.CreateLoanView.as_view()),
    path("loans/<int:book_id>/", views.ReturnLoanView.as_view()),
]
