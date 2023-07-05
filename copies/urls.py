from django.urls import path
from loans.views import LoanView

urlpatterns = [
    path("books/<int:pk>/loans/", LoanView.as_view(), name="copy-loans"),
]
