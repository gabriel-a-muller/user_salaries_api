from rest_framework import serializers
from users.models import User
from salary.serializers import SalarySerializer


class UserSerializer(serializers.ModelSerializer):
    salaries = SalarySerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'cpf', 'name', 'born_date', 'salaries']

    def validate_cpf(self, value: str) -> str:
        if not isinstance(value, str):
            raise serializers.ValidationError
        value = value.replace('.', '').replace('-', '')
        return value
