from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path("books/<int:pk>/loans/", views.CreateLoanView.as_view()),
    # path("loans/<int:book_id>/", views.ReturnLoanView.as_view()),
    path("loans/", views.LoanView.as_view()),
]
