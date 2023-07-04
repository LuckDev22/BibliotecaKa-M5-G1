from django.shortcuts import render
from rest_framework import generics

from .models import Loan
from .serializers import LoanSerializer

# Create your views here.
class LoanView(generics.ListCreateView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer



    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoanDetailView(generics.RetrieveView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer



