from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("",csrf_exempt(views.ListUserAPIView.as_view()),name="user_list"),
    path("<int:pk>",csrf_exempt(views.GetUserAPIView.as_view()),name="user_get"),
    path("create", csrf_exempt(views.CreateUserAPIView.as_view()),name="user_create"),
    path("update/<int:pk>",csrf_exempt(views.UpdateUserAPIView.as_view()),name="update_user"),
    path("delete/<int:pk>",csrf_exempt(views.DeleteUserAPIView.as_view()),name="delete_user")
]
