from rest_framework import serializers

from goat_farm.models import CustomUser, Goat, Health


class HealthSerializer(serializers.ModelSerializer):
    goat_id = serializers.PrimaryKeyRelatedField(queryset=Goat.objects.all(), source="goat", required=True)
    manager_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source="manager", required=False)

    class Meta:
        model = Health
        fields = ['id', 'date', 'title', 'description', 'treatment', 'goat_id', 'manager_id']

    def validate(self, data):
        user = self.context['request'].user
        if user.user_type == 'manager':
            if data["goat"].manager_id == user.id:
                data["goat_id"] = data["goat"].id
            else:
                raise serializers.ValidationError({"goat_id": "This field should be assigned of your our own goat."})
            data['manager_id'] = user.id
            data['manager'] = user
        elif user.user_type == 'admin':
            if 'goat' in data:
                goat = data['goat']
                data["goat_id"] = goat.id
                manager = CustomUser.objects.get(pk=goat.manager_id)
                if manager.DoesNotExist and manager.user_type != 'manager':
                    raise serializers.ValidationError({"manager_id": "This field should be assigned to a manager user."})
                data['manager_id'] = goat.manager_id
                data['manager'] = manager
            else:
                raise serializers.ValidationError({"manager_id": "This field is required for admin users."})

        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.context['request'].user.user_type == 'manager':
            ret.pop('manager_id', None)
        return ret
