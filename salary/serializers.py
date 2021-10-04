from rest_framework import serializers
from salary.models import Salary


class SalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Salary
        fields = ['id', 'user', 'salary', 'discounts', 'date']
        lookup_field = 'user'

    def validate(self, data: dict) -> dict:
        try:
            salary = data['salary']
        except:
            existing_data = self.to_representation(self.instance)
            salary = existing_data['salary']
        try:
            discounts = data['discounts']
        except:
            existing_data = self.to_representation(self.instance)
            discounts = existing_data['discounts']

        if salary < discounts:
            raise serializers.ValidationError(
                'Discount bigger than Salary!')
        return data


class SalarySerializerEdit(SalarySerializer):

    class Meta(SalarySerializer.Meta):
        read_only_fields = ['user']


class AverageSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    average = serializers.FloatField()


class AverageSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    average = serializers.FloatField()
