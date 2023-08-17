from django.contrib import admin
from .models import BusDetailsModels
# Register your models here.
class BusDetailsAdmin(admin.ModelAdmin):
    list_display = ['model','hp','color','price']


admin.site.register(BusDetailsModels,BusDetailsAdmin)