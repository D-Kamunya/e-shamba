from rest_framework.response import Response
from rest_framework import generics
from .serializer import ScheduleSerializer
from .models import Schedule
# schedule Create API

class ScheduleAPI(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleCreateApi(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# schedule List API

# schedule Update API
class ScheduleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# Schedule Delete API
class ScheduleDeleteApi(generics.DestroyAPIView):
   queryset = Schedule.objects.all()
   serializer_class = ScheduleSerializer


