from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("",csrf_exempt(views.ListSalaryAPIView.as_view()),name="salary_list"),
    path("<int:pk>",csrf_exempt(views.GetSalaryAPIView.as_view()),name="salary_get"),
    path("create", csrf_exempt(views.CreateSalaryAPIView.as_view()),name="salary_create"),
    path("update/<int:pk>",csrf_exempt(views.UpdateSalaryAPIView.as_view()),name="update_salary"),
    path("delete/<int:pk>",csrf_exempt(views.DeleteSalaryAPIView.as_view()),name="delete_salary"),
    path("average_salary", csrf_exempt(views.AverageSalaryAPIView.as_view()), name="average_salary"),
    path("average_discounts", csrf_exempt(views.AverageDiscountsAPIView.as_view()), name="average_discounts"),
    path("min", csrf_exempt(views.MinSalaryAPIView.as_view()), name="min"),
    path("max", csrf_exempt(views.MaxSalaryAPIView.as_view()), name="max"),
]