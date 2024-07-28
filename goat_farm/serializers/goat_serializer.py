from rest_framework import serializers

from goat_farm.models import CustomUser, Goat


class GoatSerializer(serializers.ModelSerializer):
    manager_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='manager', required=False)

    class Meta:
        model = Goat
        fields = ['id', 'name', 'breed', 'date_of_birth', 'manager_id']

    def validate(self, data):
        user = self.context['request'].user

        if user.user_type == 'manager':
            data['manager_id'] = user.id
        elif user.user_type == 'admin':
            if 'manager' in data:
                manager = data['manager']
                if manager.user_type != 'manager':
                    raise serializers.ValidationError({"manager_id": "This field should be assigned to a manager user."})
            else:
                raise serializers.ValidationError({"manager_id": "This field is required for admin users."})

        return data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if self.context['request'].user.user_type == 'manager':
            ret.pop('manager_id', None)
        return ret
