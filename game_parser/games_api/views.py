from parser_app.models import Games
from rest_framework import viewsets
from rest_framework import permissions
from games_api.serializers import GameSerializer


# Create your views here.

class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.BasePermission]