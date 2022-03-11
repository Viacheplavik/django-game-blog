from django.shortcuts import render
from .models import Games


# from game_parser.game_parser.managers.igdb_manager import IGDB_manager
# Create your views here.


def games_view(request):
    # IGDB_manager.create_objects_from_igdb_response()
    all_games = Games.objects.all()
    return render(request, 'games.html', {'all_games': all_games})
