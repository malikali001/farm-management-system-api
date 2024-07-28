from rest_framework import generics

from goat_farm.models import CustomUser
from goat_farm.permissions import IsAdmin, IsOwner
from goat_farm.serializers import CustomUserSerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method in ('GET', 'PATCH', 'PUT'):
            return [IsOwner()]
        return [IsAdmin()]
