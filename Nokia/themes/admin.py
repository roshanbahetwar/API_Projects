from django.contrib import admin
from .models import ThemesDetailsModels

# Register your models here.
class ThemesDetailsAdmin(admin.ModelAdmin):
    list_display = ['name','age','topic','date','email','mobile']

admin.site.register(ThemesDetailsModels,ThemesDetailsAdmin)