from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from .models import CategoryChoices


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Email already registered.",
            )
        ]
    )
    cpf = serializers.IntegerField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="CPF already registered.",
            )
        ]
    )
    telephone = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Telephone already registered.",
            )
        ]
    )
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    date_birth = serializers.DateField(allow_null=True, default=None)
    is_student = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    category_preference = serializers.CharField(
        allow_null=True, default=CategoryChoices.OUTROS
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "cpf",
            "telephone",
            "date_birth",
            "category_preference",
            "is_student",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop("password")
        validated_data["is_superuser"] = validated_data.get("is_employee", False)
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance: User, validated_data):
        for key, values in validated_data.items():
            if key == "password":
                values = make_password(values)
            setattr(instance, key, values)
        instance.save()
        return instance
