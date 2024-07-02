from django.contrib import admin
from .models import MobileDetailsModel

# Register your models here.
class MobileDetailsAdmin(admin.ModelAdmin):
    list_display = ['prduct_name','ram','rom','price']


admin.site.register(MobileDetailsModel,MobileDetailsAdmin)