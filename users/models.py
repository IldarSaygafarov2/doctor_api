from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	surname = models.CharField(verbose_name='Отчество', max_length=100)
	phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)
	birth_date = models.CharField(verbose_name='Дата рождения', max_length=20, null=True, blank=True)
	email = models.EmailField(unique=True)
	
	REQUIRED_FIELDS = ['phone_number']	
	USERNAME_FIELD = 'email'
	
	class Meta:
		unique_together = ['email']