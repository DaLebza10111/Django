from django.db import models

# Create your models here.
class Tour(models.Model):
    #Origin country and destination, Number of nights, price
    country_of_origin = models.CharField(max_length=64)
    country_of_destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    #string representation of the records
    def __str__(self) -> str:
        return (f"ID:{self.id} from {self.country_of_origin} to {self.country_of_destination} duration {self.number_of_nights} nights and the total cost ${self.price}")