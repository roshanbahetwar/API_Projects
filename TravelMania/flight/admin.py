from django.contrib import admin
from .models import FlightDetailsModel

# Register your models here.
class FlightDetailsAdmin(admin.ModelAdmin):
    list_display = ['fname','start','end']


admin.site.register(FlightDetailsModel,FlightDetailsAdmin)