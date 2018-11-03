from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    iso_code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    continent = models.CharField(max_length=20)
