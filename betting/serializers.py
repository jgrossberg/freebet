from django.contrib.auth.models import User, Group
from betting.models import Line, Game
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ['type', 'game', 'team', 'points', 'odds', 'side']
        depth = 1

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'team1', 'team2']
        depth = 1
