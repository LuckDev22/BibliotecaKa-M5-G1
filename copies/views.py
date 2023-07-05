from django.shortcuts import render
from rest_framework import generics
from .models import Copy
from .serializers import CopySerializer


# Create your views here.

class CopyView(generics.ListCreateAPIView):
     queryset = Copy.objects.all()
     serializer_class = CopySerializer


     lookup_url_kwarg = "pk"


     def perform_create(self, serializer):
          serializer.save(book_id=self.kwargs.get("pk"))


