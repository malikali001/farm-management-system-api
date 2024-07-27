from rest_framework import serializers

from goat_farm.models import CustomUser, Goat, Health


class HealthSerializer(serializers.ModelSerializer):
    goat_id = serializers.PrimaryKeyRelatedField(queryset=Goat.objects.all(), source="goat")
    manager_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source="manager")

    class Meta:
        model = Health
        fields = ['id', 'date', 'title', 'description', 'treatment', 'goat_id', 'manager_id']

