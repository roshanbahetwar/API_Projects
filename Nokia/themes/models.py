from django.db import models

# Create your models here.
class ThemesDetailsModels(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    topic = models.CharField(max_length=25)
    date = models.DateField()
    email = models.EmailField()
    mobile = models.BigIntegerField()