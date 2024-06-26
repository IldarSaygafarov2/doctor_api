from django.contrib import admin
from .models import Doctor, DoctorInfo, DoctorDirection, DoctorCategory, Symptom


class DoctorInfoInline(admin.TabularInline):
    model = DoctorInfo
    extra = 1


class DoctorDirectionInline(admin.TabularInline):
    model = DoctorDirection
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'display_full_name', 'age']
    list_display_links = ['pk', 'display_full_name']
    inlines = [DoctorDirectionInline, DoctorInfoInline]

    def display_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name} {obj.surname}'


@admin.register(DoctorCategory)
class DoctorCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk', 'title']


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk']


admin.site.register(Doctor, DoctorAdmin)
