from django.db import models
from django.db.models import Model


# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=25)
    size = models.PositiveIntegerField()
