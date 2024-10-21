from rest_framework import serializers
from twitter.models.post import Post
from twitter.models.user import User
from twitter.serializers.user_serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['author','body', 'created_at', 'author_name']
        