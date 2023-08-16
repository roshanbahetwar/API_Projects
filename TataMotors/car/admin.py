from django.contrib import admin
from .models import CarDetailsModel

# Register your models here.
class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ['model','hp','color','price']

admin.site.register(CarDetailsModel,CarDetailsAdmin)