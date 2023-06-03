from rest_framework import serializers
from .models import FeatureDetailsModel

class FeatureDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = FeatureDetailsModel
        fields = '__all__'