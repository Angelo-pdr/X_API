from twitter.models.users import User

from twitter.serializers.user_serializer import UserSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('id')