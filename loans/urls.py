from django.urls import path

from . import views

urlpatterns = [
    path("loans/<int:copy_id>/", views.LoanView.as_views())

]