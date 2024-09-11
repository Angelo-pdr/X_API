from rest_framework import serializers
from twitter.models.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']