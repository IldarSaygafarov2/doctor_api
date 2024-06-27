from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.DoctorListAPIView.as_view(), name='doctors-list'),
    path('categories/', views.DoctorCategoryAPIView.as_view(), name='doctors-categories'),
    path('symptoms/', views.SymptomAPIView.as_view(), name='symptoms'),
]