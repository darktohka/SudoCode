from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    country = models.CharField(max_length=20)
