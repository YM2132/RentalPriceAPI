from django.db import models
from djongo.models import ObjectIdField

# Create your models here.
class Rental(models.Model):
    _id = ObjectIdField()
    price_pw = models.IntegerField()
    price_pm = models.IntegerField()
    location = models.TextField(max_length=250)
    property_type = models.TextField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.property_type
