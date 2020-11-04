from rest_framework import  serializers
from .models import Schedule,Crop,Post,Product,Prod_rec,Crop_prd
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'email')        

class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False) 
    class Meta:
        model = Schedule
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Crop
        fields = '__all__'
  
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__' 
  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      fields = ('id','name', 'photo', 'category', 'price', 'crops', 'upload_date')
      model = Product  


class ProductRecSerializer(serializers.ModelSerializer):
    class Meta:
      fields = '__all__'
      model = Prod_rec



class CropPrdSerializer(serializers.ModelSerializer):
    class Meta:
      fields = '__all__'
      model = Crop_prd

  

