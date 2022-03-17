from django.shortcuts import render
from .models import Games
from .managers.igdb_manager import IgdbManager


def games_view(request):
    igdb_manager = IgdbManager()
    igdb_manager.create_objects_from_igdb_response()
    games = Games.objects.all()[:10]
    return render(request, 'games.html', {'games': games})
