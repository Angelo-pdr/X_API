from rest_framework import serializers
from twitter.models.post import Post
from twitter.models.users import User
from twitter.serializers.user_serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    usuario = User
    user = UserSerializer(usuario , read_only=True, many=True)
    class Meta:
        model = Post
        fields = ['user','author', 'body', 'created_at']
        