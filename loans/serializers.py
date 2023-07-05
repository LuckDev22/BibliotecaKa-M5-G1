from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from copies.serializers import CopySerializer


class LoanSerializer(serializers.ModelSerializer):
    copy = CopySerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = ["id", "data_emprestimo", "data_devolucao", "copy", "user"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
