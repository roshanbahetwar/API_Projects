from django.db import models

# Create your models here.
class SalesDataModel(models.Model):
    employeeNumber = models.IntegerField()
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    extension = models.CharField(max_length=50)
    email = models.EmailField()
    officeCode = models.IntegerField()
    jobTitle = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    reportsTo = models.IntegerField()
    reportToLastName = models.CharField(max_length=30)
    reportToFirstName = models.CharField(max_length=30)
