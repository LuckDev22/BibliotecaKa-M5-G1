from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import IsAccountOwner
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.views import Request, Response


# Create your views here.
class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        password = self.request.data.get("password")
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()
