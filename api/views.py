
from .serializers import DoctorGetSerializer, DoctorCategorySerializer, SymptomSerializer
from rest_framework import generics
from .models import Doctor, DoctorCategory, Symptom
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Doctors API'])
class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorGetSerializer


@extend_schema(tags=['Doctors API'])
class DoctorCategoryAPIView(generics.ListAPIView):
    queryset = DoctorCategory.objects.all()
    serializer_class = DoctorCategorySerializer

@extend_schema(tags=['Doctors API'])
class SymptomAPIView(generics.ListAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

