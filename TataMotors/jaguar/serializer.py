from rest_framework import serializers
from .models import JaguarModel

class JaguarDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = JaguarModel
        fields = '__all__'