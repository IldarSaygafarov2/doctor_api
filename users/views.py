from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserGetSerializer, UserRegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class UserListAPIView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserGetSerializer


class UserRegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer


class UserLogoutView(APIView):
	def post(self, request):
		try:
			refresh_token = request.data['refresh_token']
			token = RefreshToken(refresh_token)
			token.blacklist()
			return Response({'message': "Successfully logged out"}, status=205)
		except Exception as e:
			return Response(status=400)