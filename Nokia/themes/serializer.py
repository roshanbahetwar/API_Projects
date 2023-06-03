from rest_framework import serializers
from .models import ThemesDetailsModels

class ThemesDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = ThemesDetailsModels
        fields = '__all__'