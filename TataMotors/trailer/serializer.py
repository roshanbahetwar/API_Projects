from rest_framework import serializers
from .models import TrailerDetailsModel

class TrailerDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = TrailerDetailsModel
        fields = '__all__'