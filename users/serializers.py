from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['pk', 'first_name', 'last_name', 'surname']


class UserRegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Email must be unique'
        )
        ],
    )
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)
	
	
	class Meta:
		model = User
		fields = ['first_name', 'email', 'phone_number', 'birth_date', 'password', 'password2']
	
	
	def validate(self, attrs):
		password_1 = attrs.pop('password')
		password_2 = attrs.pop('password2')
		if password_1 != password_2:
			raise serializers.ValidationError({'password': 'Password fields didn"t match'})
		
		attrs['password'] = password_1
		return attrs
	
	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		return user
		