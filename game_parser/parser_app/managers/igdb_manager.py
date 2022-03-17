from ..models import Games
from ..parser import IgdbWrapper

CLIENT_ID = 'bu2vadve064duzrmf81rfdrsec76sq'
SECRETE_CODE = '9z5v1rhgi93g5r42d9p8y23qb33xvn'

class IgdbManager:
    @staticmethod
    def create_objects_from_igdb_response():
        igdb_wrapper = IgdbWrapper(client_id=CLIENT_ID, secret_code=SECRETE_CODE)
        games_list = igdb_wrapper.get_games()
        for game in games_list:
            Games.objects.create(
                name=game['name'],
                twitch_url=game['twitch_url'],
                summary=game['summary']
            )
