from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserGetSerializer, UserRegisterSerializer
from .models import User


class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserGetSerializer


class UserRegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer