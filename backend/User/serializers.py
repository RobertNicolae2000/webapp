from djoser.serializers import UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('email', 'id', 'username', 'is_staff')