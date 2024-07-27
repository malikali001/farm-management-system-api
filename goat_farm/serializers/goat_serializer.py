from rest_framework import serializers

from goat_farm.models import CustomUser, Goat


class GoatSerializer(serializers.ModelSerializer):
    manager_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Goat
        fields = ['id', 'name', 'breed', 'date_of_birth', 'manager_id']
