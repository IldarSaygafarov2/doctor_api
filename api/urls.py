from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.DoctorListAPIView.as_view(), name='doctors-list'),
]