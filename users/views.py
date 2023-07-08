from rest_framework_simplejwt.authentication import JWTAuthentication
from .permission import IsAccountOwner
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.views import Request, Response


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
            
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_blocked = False
        instance.blocked_until = None
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)