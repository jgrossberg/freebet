from django.contrib.auth.models import User, Group
from betting.models import Line, Game, Team
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
    game = serializers.StringRelatedField(many=False)
    team = serializers.StringRelatedField(many=False)
    class Meta:
        model = Line
        fields = ['type', 'game', 'team', 'points', 'odds', 'side']
        depth = 1

class GameSerializer(serializers.ModelSerializer):
    team1 = serializers.StringRelatedField(many=False)
    team2 = serializers.StringRelatedField(many=False)
    class Meta:
        model = Game
        fields = ['team1', 'team2']
        depth = 1


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'city', 'name']
