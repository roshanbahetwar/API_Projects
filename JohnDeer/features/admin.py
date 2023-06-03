from django.contrib import admin
from .models import FeatureDetailsModel

# Register your models here.
class FeatureDetailsAdmin(admin.ModelAdmin):

    list_display = ['model','hp','color','price']

admin.site.register(FeatureDetailsModel,FeatureDetailsAdmin)