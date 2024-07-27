from rest_framework import generics

from goat_farm.models import Goat
from goat_farm.serializers import GoatSerializer


class GoatList(generics.ListCreateAPIView):
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer


class GoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
