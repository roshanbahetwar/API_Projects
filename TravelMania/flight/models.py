from django.db import models

# Create your models here.
class FlightDetailsModel(models.Model):
    fname = models.CharField(max_length=25)
    start = models.CharField(max_length=25)
    end = models.CharField(max_length=25)