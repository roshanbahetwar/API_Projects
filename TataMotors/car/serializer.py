from rest_framework import serializers
from .models import CarDetailsModel

class CarDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = CarDetailsModel
        fields = '__all__'