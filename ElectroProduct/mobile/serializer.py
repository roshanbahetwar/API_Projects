from rest_framework import serializers
from .models import MobileDetailsModel

class MobileDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = MobileDetailsModel
        fields = '__all__'