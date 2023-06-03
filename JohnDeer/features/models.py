from django.db import models

# Create your models here.
class FeatureDetailsModel(models.Model):
    model = models.CharField(max_length=20)
    hp = models.IntegerField()
    color = models.CharField(max_length=25)
    price = models.IntegerField()