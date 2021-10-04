from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListSalaryAPIView.as_view(),name="salary_list"),
    path("create/", views.CreateSalaryAPIView.as_view(),name="salary_create"),
    path("update/<int:pk>/",views.UpdateSalaryAPIView.as_view(),name="update_salary"),
    path("delete/<int:pk>/",views.DeleteSalaryAPIView.as_view(),name="delete_salary"),
    path("average_salary/", views.AverageSalaryAPIView.as_view(), name="average_salary"),
    path("average_discounts/", views.AverageDiscountsAPIView.as_view(), name="average_discounts"),
    path("min/", views.MinSalaryAPIView.as_view(), name="min"),
    path("max/", views.MaxSalaryAPIView.as_view(), name="max"),
]