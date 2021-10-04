from rest_framework import generics, views
from rest_framework.response import Response
from salary import serializers
from salary.models import Salary


class ListSalaryAPIView(generics.ListAPIView):
    """
    This endpoint list all of the available salaries from the database
    """
    queryset = Salary.objects.all().order_by('-id')
    serializer_class = serializers.SalarySerializer


class GetSalaryAPIView(generics.RetrieveAPIView):
    """
    This endpoint will get a specific salary by passings its id
    """
    queryset = Salary.objects.all()
    serializer_class = serializers.SalarySerializer


class CreateSalaryAPIView(generics.CreateAPIView):
    """
    This endpoint allows for creation of a salary
    """
    queryset = Salary.objects.all()
    serializer_class = serializers.SalarySerializer


class UpdateSalaryAPIView(generics.UpdateAPIView):
    """
    This endpoint allows for updating a specific salary by
    passing in the id of the salary to update
    """
    queryset = Salary.objects.all()
    serializer_class = serializers.SalarySerializerEdit


class DeleteSalaryAPIView(generics.DestroyAPIView):
    """
    This endpoint allows for deletion of a
    specific Salary from the database
    """
    queryset = Salary.objects.all()
    serializer_class = serializers.SalarySerializer


class AverageSalaryAPIView(views.APIView):
    """
    This endpoint will return the total Average Salary
    """
    def get(self, request):
        data = Salary.objects.get_salary_average()
        results = serializers.AverageSerializer(data).data
        return Response(results)


class AverageDiscountsAPIView(views.APIView):
    """
    This endpoint will return the total Average Discounts
    """
    def get(self, request):
        data = Salary.objects.get_discounts_average()
        results = serializers.AverageSerializer(data).data
        return Response(results)


class MinSalaryAPIView(views.APIView):
    """
    This endpoint will return the lower Salary
    """
    def get(self, request):
        data = Salary.objects.get_min_salary()
        results = serializers.SalarySerializer(data).data
        return Response(results)


class MaxSalaryAPIView(views.APIView):
    """
    This endpoint will return the higher Salary
    """
    def get(self, request):
        data = Salary.objects.get_max_salary()
        results = serializers.SalarySerializer(data).data
        return Response(results)
