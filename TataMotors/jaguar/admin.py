from django.contrib import admin
from .models import JaguarModel

# Register your models here.
class JaguarDetailsAdmin(admin.ModelAdmin):
    list_display = ['model','hp','color','price']


admin.site.register(JaguarModel,JaguarDetailsAdmin)