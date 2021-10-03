from django.core.exceptions import ValidationError
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'cpf', 'name', 'born_date']

    def validate_cpf(self, value: str) -> str:
        if not isinstance(value, str):
            raise ValidationError
        value = value.replace('.', '').replace('-', '')
        return value
