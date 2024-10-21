from django.forms import ValidationError
from rest_framework import serializers
from twitter.models.user import User
from django.contrib.auth import get_user_model, authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']