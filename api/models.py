from django.db import models
from users.models import User


class Doctor(models.Model):
	profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
	image = models.ImageField(verbose_name='Фото', upload_to='doctors/', null=True, blank=True)
	age = models.PositiveSmallIntegerField(verbose_name='Возраст')
	disease = models.CharField(verbose_name='Болезнь', max_length=150, null=True, blank=True)
	doctor = models.CharField(verbose_name='Доктор', max_length=150, null=True, blank=True)
	education = models.CharField(verbose_name='Образование', max_length=200, null=True, blank=True)
	work = models.CharField(verbose_name='Работа', max_length=500, null=True, blank=True)
	information = models.TextField(verbose_name='Информация', null=True, blank=True)
	
	def __str__(self):
		return f'{self.profile.first_name} {self.profile.last_name} {self.profile.surname}'
	
	class Meta:
		verbose_name = 'Доктор'
		verbose_name_plural = 'Доктора'


class DoctorDirection(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	direction = models.CharField(max_length=150, verbose_name='Направление')
	
	def __str__(self):
		return self.direction
	
	class Meta:
		verbose_name = 'Направление'
		verbose_name_plural = 'Направления'


class DoctorInfo(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	info = models.CharField(max_length=150, verbose_name='Инфо')

	def __str__(self):
		return self.info
	
	class Meta:
		verbose_name = 'Инфо'
		verbose_name_plural = 'Инфо'
	