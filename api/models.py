from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Restaurant(models.Model):

    id = models.TextField(primary_key=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    name = models.TextField()
    site = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()