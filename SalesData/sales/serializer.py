from rest_framework import serializers
from .models import SalesDataModel

class SalesDataSer(serializers.ModelSerializer):
    class Meta:
        model = SalesDataModel
        fields = '__all__'