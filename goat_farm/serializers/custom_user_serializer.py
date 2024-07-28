from rest_framework import serializers

from goat_farm.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'user_type', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if validated_data['user_type'] == 'admin':
            validated_data['is_superuser'] = True
            validated_data['is_staff'] = True

        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        request_user = self.context['request'].user
        if 'user_type' in validated_data and request_user.is_superuser:
            if validated_data['user_type'] == 'admin':
                validated_data['is_superuser'] = True
                validated_data['is_staff'] = True
            elif validated_data['user_type'] == 'manager':
                validated_data['is_superuser'] = False
                validated_data['is_staff'] = False
        else:
            validated_data.pop('user_type', None)

        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
