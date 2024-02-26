from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, label="username")
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(
            self.context.get("request"), username=username, password=password
        )
        if not user:
            raise serializers.ValidationError(
                "Unable to log in with provided credentials."
            )
        return data


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if not password1 == password2:
            raise serializers.ValidationError("Passwords must be equal")
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                "User already exists pick another username"
            )

        return data
