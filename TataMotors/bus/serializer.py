from rest_framework import serializers
from .models import BusDetailsModels

class BusDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = BusDetailsModels
        fields = '__all__'
