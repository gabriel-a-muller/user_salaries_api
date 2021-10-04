from rest_framework import serializers
from salary.models import Salary


class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = ['id', 'user', 'salary', 'discounts', 'date']
        lookup_field = 'user'

    def validate(self, data: dict) -> dict:
        if data['salary'] < data['discounts']:
            raise serializers.ValidationError(
                'Discount bigger than Salary!')
        return data


class AverageSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    average = serializers.FloatField()


class AverageSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    average = serializers.FloatField()
