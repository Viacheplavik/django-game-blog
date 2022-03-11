from django.db import models
# from .parser import parse_games
# from itertools import islice
# Create your models here.


class Games(models.Model):
    game_name = models.CharField(max_length=20)
    twitch_url = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)





