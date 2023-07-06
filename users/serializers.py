from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from .models import CategoryChoices


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
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
            "is_blocked",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        is_student = validated_data.pop("is_student", False)
        validated_data["is_superuser"] = not is_student
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)
        user.is_student = is_student
        user.save()
        return user


def update(self, instance: User, validated_data):
    for key, values in validated_data.items():
        if key == "password":
            values = make_password(values)
        setattr(instance, key, values)
    instance.save()
    return instance
