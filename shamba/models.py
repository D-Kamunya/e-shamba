from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from users.models import Profile
from pyuploadcare.dj.models import ImageField

class Product(models.Model):
    """
    Product class to define Product Objects
    """
    tags= (
        ('Pesticide', 'Pesticide'),
        ('Fungicide', 'Fungicide'),
        ('Fertilizer', 'Fertilizer'),
        ('Booster', 'Booster')
    )

    
    name = models.CharField(max_length =150)
    photo = ImageField(blank=True, manual_crop="")
    category = models.CharField(choices=tags,max_length =150,default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    crops = models.CharField(max_length =150)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

