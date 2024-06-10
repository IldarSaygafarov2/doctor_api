from django.shortcuts import render
from rest_framework.response import Response
from .serializers import DoctorGetSerializer
from rest_framework import generics
from .models import Doctor


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorGetSerializer
