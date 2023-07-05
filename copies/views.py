from django.shortcuts import render
from rest_framework import generics
from .models import Copy
from .serializers import CopySerializer


class CopyView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyDetailView(generics.RetrieveAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
