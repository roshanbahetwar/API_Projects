from django.db import models

# Create your models here.
class MobileDetailsModel(models.Model):
    prduct_name = models.CharField(max_length=25)
    ram = models.IntegerField()
    rom = models.IntegerField()
    price = models.IntegerField()