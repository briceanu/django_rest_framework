
import re
from rest_framework import serializers
from django.contrib.auth.models import User

class DriverSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    date_joined = serializers.DateTimeField(read_only=True)  # Read-only, automatically handled by Django
    

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'date_joined']

    def validate_password(self, value):
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain at least one number")
        if len(value) <= 6:
            raise serializers.ValidationError("Password must be at least 7 characters")
        return value

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"passwords": "Passwords don't match"})
        if User.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError({"username": "Username already exists"})
        return data

    def validate_username(self, value):
    # Define a regex to allow only alphanumeric characters and a few safe symbols
        if not re.match(r'^[\w.@+-]+$', value):
            raise serializers.ValidationError(
            "Username contains invalid characters. Only letters, numbers, and @/./+/-/_ are allowed. No space"
            )

        return value
                


    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password as it's not needed for user creation
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


 