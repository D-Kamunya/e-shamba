from rest_framework import  serializers
from .models import Schedule,Crop,Post,Product,Prod_rec,Crop_prd,Post_Comment,Crop_activity
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'email')        

class ScheduleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Schedule
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
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



class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
      fields = '__all__'
      model = Post_Comment



class CropActivitySerializer(serializers.ModelSerializer):
    class Meta:
      fields = '__all__'
      model = Crop_activity


  

