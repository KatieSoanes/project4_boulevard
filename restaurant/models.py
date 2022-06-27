from django.db import models


class Restaurant(models.Model):
    no_of_tables = models.IntegerField(default=0)


class Reservation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    time = models.DateTimeField()
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    