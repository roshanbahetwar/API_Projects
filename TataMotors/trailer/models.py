from django.db import models

# Create your models here.
class TrailerDetailsModel(models.Model):
    model = models.CharField(max_length=10)
    no_of_wheels = models.IntegerField()
    hp = models.IntegerField()
    price = models.IntegerField()