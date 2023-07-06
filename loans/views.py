from django.shortcuts import render
from rest_framework import generics

from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permission import IsAccountOwner
from .models import Loan
from .serializers import LoanSerializer
from copies.models import Copy

# Create your views here.
class LoanView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]


    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    
    def perform_create(self, serializer):
        copy = Copy.objects.get(pk=self.kwargs.get("copy_id"))
        serializer.save(user=self.request.user, copy=copy)




