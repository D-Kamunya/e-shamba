from rest_framework import  serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id','name', 'photo', 'category', 'price', 'crops', 'upload_date')
    model = Product