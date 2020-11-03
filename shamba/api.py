from rest_framework import generics
from rest_framework.response import Response
from .serializer import ScheduleSerializer
from .models import Schedule
# schedule Create API
class ScheduleCreateApi(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# schedule List API
class ScheduleListAPI(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# schedule Update API
class ScheduleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
# Schedule Delete API
class ScheduleDeleteApi(generics.DestroyAPIView):
   queryset = Schedule.objects.all()
   serializer_class = ScheduleSerializer