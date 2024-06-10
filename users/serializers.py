from rest_framework import serializers
from .models import User


class UserGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['pk', 'first_name', 'last_name', 'surname']