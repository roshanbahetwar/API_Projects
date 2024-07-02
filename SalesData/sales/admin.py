from django.contrib import admin
from .models import SalesDataModel

# Register your models here.
class SalesDataAdmin(admin.ModelAdmin):

    list_display = ['employeeNumber','lastName','firstName','extension','email','officeCode','jobTitle','city','phone','reportsTo','reportToLastName','reportToFirstName']

admin.site.register(SalesDataModel,SalesDataAdmin)