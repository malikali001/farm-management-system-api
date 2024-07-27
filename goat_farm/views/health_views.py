from rest_framework import generics

from goat_farm.models import Health
from goat_farm.serializers import HealthSerializer


class HealthList(generics.ListCreateAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer


class HealthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
