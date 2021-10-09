from rest_framework import generics, serializers
from users.serializers import UserSerializer
from users.models import User


class ListUserAPIView(generics.ListAPIView):
    """
    This endpoint list all of the available users from the database
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class GetUserAPIView(generics.RetrieveAPIView):
    """
    This endpoint will get a specific user by passings its id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    """
    This endpoint allows for creation of a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserAPIView(generics.UpdateAPIView):
    """
    This endpoint allows for updating a specific user by
    passing in the id of the user to update
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        if User.objects.filter(cpf=request.data['cpf']).exclude(id=kwargs['pk']).exists():
            raise serializers.ValidationError(
                "Duplicate entry for cpf: " + request.data['cpf'])
        return super().patch(request, *args, **kwargs)


class DeleteUserAPIView(generics.DestroyAPIView):
    """
    This endpoint allows for deletion of a
    specific User from the database
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer