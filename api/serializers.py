from rest_framework import serializers
from .models import Doctor, DoctorInfo, DoctorDirection, DoctorCategory, Symptom



class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['pk', 'doctor', 'name', 'img']


class DoctorInfoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorInfo
        fields = ['info']


class DoctorDirectionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDirection
        fields = ['direction']


class DoctorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorCategory
        fields = ['pk', 'title']


class DoctorGetSerializer(serializers.ModelSerializer):

    info = DoctorInfoGetSerializer(many=True)
    direction = DoctorDirectionGetSerializer(many=True)

    class Meta:
        model = Doctor
        fields = [
            'pk',
            'fullname',
            'age',
            'image',
            'disease',
            'doctor',
            'education',
            'work',
            'information',
            'info',
            'direction',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        info = [item['info'] for item in data['info']]
        directions = [item['direction'] for item in data['direction']]
        data['info'] = info
        data['direction'] = directions
        return data

