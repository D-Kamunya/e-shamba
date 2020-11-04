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



class Prod_rec(models.Model):
    """
    Prod_rec class to define Product product recommendations Objects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rec_crops = models.CharField(max_length =150)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id



class Crop(models.Model): 
    """
    Crop class to define crop Objects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length =150)
    photo = ImageField(blank=True, manual_crop="")
    details = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Crop_prd(models.Model):
    """
    Crop_prd class to define Products used on specific crop Objects
    """
    crop= models.ForeignKey(Crop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id  



class Post(models.Model):
    """
    Post class to define post Objects
    """
    name = models.CharField(max_length =150)
    details = models.TextField()
    user = models.ForeignKey(User,
    on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    comment_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
      return self.id         



class Crop_activity(models.Model):
    """
    Crop_activity class to define specific crop activities Objects
    """
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    activity = models.TextField()
    activity_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id



class Schedule(models.Model): 
    """
    Schedule class to define scheduled activities Objects
    """
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    name = models.CharField(max_length =150)
    details = models.TextField()
    schedule_date = models.DateTimeField()

    def __str__(self):
        return self.id

