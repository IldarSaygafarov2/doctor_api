from django.contrib import admin
from .models import Doctor, DoctorInfo, DoctorDirection


class DoctorInfoInline(admin.TabularInline):
	model = DoctorInfo
	extra = 1


class DoctorDirectionInline(admin.TabularInline):
	model = DoctorDirection
	extra = 1
	
	
class DoctorAdmin(admin.ModelAdmin):
	list_display = ['profile', '']