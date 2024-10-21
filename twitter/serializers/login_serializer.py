from rest_framework import serializers
from twitter.models.user import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                raise serializers.ValidationError('Credenciais inválidas.')
        else:
            raise serializers.ValidationError('Por favor, preencha ambos os campos.')

        attrs['user'] = user
        return attrs