from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=20)
    twitch_url = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
