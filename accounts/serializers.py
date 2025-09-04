from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Token
from .helpers import send_confirmation_token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"]
        )
        Token.objects.create(user=user)
        send_confirmation_token(user.email, user.auth_token.token)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_confirmed_email:
            raise serializers.ValidationError("Email not confirmed")
        return {"user": user}
