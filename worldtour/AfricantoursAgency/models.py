from django.db import models

# Create your models here.
class Tour(models.Model):
    #Origin country and destination, Number of nights, price
    country_of_origin = models.CharField(max_length=64)
    country_of_destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()