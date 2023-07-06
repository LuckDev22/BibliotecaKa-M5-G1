"""from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import LoanViewList

urlpatterns = [
    path("loans/", views.LoanViewList.as_view()),
]
"""
from django.urls import path
from .views import LoanViewList

urlpatterns = [path("loans/", LoanViewList.as_view())]
