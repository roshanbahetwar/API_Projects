from django import forms
from .models import BusDetailsModels

class BusDetailsForm(forms.ModelForm):
    class Meta:
        model = BusDetailsModels
        fields = '__all__'