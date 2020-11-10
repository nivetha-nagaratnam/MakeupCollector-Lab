from django.db import models
from django.urls import reverse

# Create your models here.

class Makeup(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description =  models.TextField(max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'makeup_id': self.id})

