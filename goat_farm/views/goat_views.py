from rest_framework import generics

from goat_farm.models import Goat
from goat_farm.permissions import IsAdminOrOwner
from goat_farm.serializers import GoatSerializer


class GoatList(generics.ListCreateAPIView):
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'manager':
            return Goat.objects.filter(manager=user)
        return super().get_queryset()

    def perform_update(self, serializer):
        user = self.request.user
        if user.user_type == 'manager':
            serializer.save(manager=user)
        else:
            serializer.save()


class GoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goat.objects.all()
    serializer_class = GoatSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'manager':
            return Goat.objects.filter(manager=user)
        return super().get_queryset()

    def perform_update(self, serializer):
        user = self.request.user
        if user.user_type == 'manager':
            serializer.save(manager=user)
        else:
            serializer.save()
