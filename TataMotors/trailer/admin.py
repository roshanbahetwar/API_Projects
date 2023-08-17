from django.contrib import admin
from .models import TrailerDetailsModel
# Register your models here.
class TrailerDetailsAdmin(admin.ModelAdmin):
    list_display = ['model','no_of_wheels','hp','price']

admin.site.register(TrailerDetailsModel,TrailerDetailsAdmin)