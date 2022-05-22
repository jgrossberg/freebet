from django.contrib.auth.models import User, Group
from betting.models import Line, Game, Team
from rest_framework import viewsets
from rest_framework import permissions
from betting.serializers import UserSerializer, GroupSerializer, LineSerializer, GameSerializer, TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows betting lines to be viewed or edited.
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = [permissions.IsAuthenticated]

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows betting lines to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows betting lines to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]