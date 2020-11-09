from django.db import models

# Create your models here.

class Makeup(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description =  models.TextField(max_length=300)
    price = models.IntegerField()

