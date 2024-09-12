from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
        )


class CustomLoginSerializer(LoginSerializer): # Removes the username field and just uses email instead for the login page
    username = None
    email = serializers.EmailField(required=True)


class CustomRegisterSerializer(RegisterSerializer): # Same as above but for registration page
    username = None
