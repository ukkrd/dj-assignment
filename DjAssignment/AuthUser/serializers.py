
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# from django.contrib.auth.models import User

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'name', 'role')


    def validate_role(self, value):
        allowed_roles = ['Admin', 'Employee']
        if value not in allowed_roles:
            raise serializers.ValidationError(
                f"Invalid role. Allowed roles are: {', '.join(allowed_roles)}"
            )
        return value


    def create(self, validated_data):
        # Extract and hash password
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user


    def update(self, validated_data):
        # Extract and hash password
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)  # hash the password
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'name', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }