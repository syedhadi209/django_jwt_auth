from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', "last_name"]

    def validate(self, data):
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("First name and last name are required.")
        
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password', 'first_name', "last_name"]
