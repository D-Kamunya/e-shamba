from rest_framework import  serializers
from .models import Schedule
from .models import Crop
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

