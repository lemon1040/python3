from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    pwd = serializers.CharField(max_length=32, required=True, write_only=True)

    class Meta:
        model = User
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'
