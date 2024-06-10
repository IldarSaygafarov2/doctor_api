from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserGetSerializer
from .models import User


class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserGetSerializer
