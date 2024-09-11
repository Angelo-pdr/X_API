from twitter.models.post import Post

from twitter.serializers.post_serializer import PostSerializer
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()