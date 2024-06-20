from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
	username = models.CharField(verbose_name='Имя пользователя', max_length=100, unique=False, null=True, blank=True)
	surname = models.CharField(verbose_name='Отчество', max_length=100)
	phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)
	birth_date = models.CharField(verbose_name='Дата рождения', max_length=20, null=True, blank=True)
	email = models.EmailField(unique=True)
	
	objects = CustomUserManager()

	REQUIRED_FIELDS = []	
	USERNAME_FIELD = 'email'
	