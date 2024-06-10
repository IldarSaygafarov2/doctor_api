from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	surname = models.CharField(verbose_name='Отчество', max_length=100)
	
