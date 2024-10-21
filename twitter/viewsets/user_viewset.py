from rest_framework import status
from django.http import HttpResponse
from twitter.models.user import User
from rest_framework.response import Response

from twitter.serializers.user_serializer import UserSerializer
from twitter.serializers.login_serializer import UserLoginSerializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        fullName = request.data.get('fullName')
        email = request.data.get('email')
        password = request.data.get('password')

        if not all([username, fullName, email, password]):
            return Response({"error": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Usuário já existe."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, email=email, fullName=fullName, password=password)
            return Response({"message": "Usuário criado com sucesso."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Cria a sessão para o usuário
            from django.contrib.auth import login as auth_login
            auth_login(request, user)

            user_data = {
                'username': user.username,
                'fullName': user.fullName,
                'email': user.email,
                'id': user.id,
                'user_active': user.user_active
            }
            return Response(user_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)