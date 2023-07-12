from django.urls import path
from .views import LoanViewList

urlpatterns = [path("loans/", LoanViewList.as_view())]
