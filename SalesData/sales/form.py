from django import forms
from .models import SalesDataModel

class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesDataModel
        fields = '__all__'