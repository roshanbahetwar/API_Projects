from django.db import models

# Create your models here.
class JaguarModel(models.Model):
    model = models.CharField(max_length=10)
    hp = models.IntegerField()
    color = models.CharField(max_length=10)
    price = models.IntegerField()