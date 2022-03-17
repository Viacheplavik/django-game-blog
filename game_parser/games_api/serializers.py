from rest_framework import serializers
from parser_app.models import Games


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"
