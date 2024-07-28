from rest_framework import generics

from goat_farm.models import Health
from goat_farm.permissions import IsAdminOrOwner
from goat_farm.serializers import HealthSerializer


class HealthList(generics.ListCreateAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'manager':
            return Health.objects.filter(manager=user)
        return super().get_queryset()

    def perform_update(self, serializer):
        user = self.request.user
        if user.user_type == 'manager':
            serializer.save(manager=user)
        else:
            serializer.save()


class HealthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'manager':
            return Health.objects.filter(manager=user)
        return super().get_queryset()

    def perform_update(self, serializer):
        user = self.request.user
        if user.user_type == 'manager':
            serializer.save(manager=user)
        else:
            serializer.save()
