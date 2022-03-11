from igdb.wrapper import IGDBWrapper
from .models import Games

import json
import requests

with open('.secrets', 'r') as secrets:
    secrets_json = json.load(secrets)

CLIENT_ID = secrets_json['client_id']
SECRET_CODE = secrets_json['secret_code']

wrapper = IGDBWrapper(client_id=CLIENT_ID, auth_token=SECRET_CODE)

token_response = requests.request("POST",
                                  f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={SECRET_CODE}&"
                                  f"grant_type=client_credentials").json()

access_token = token_response['access_token']

headers = {
    'Client-ID': CLIENT_ID,
    'Authorization': f"Bearer {access_token}"
}

body_games = 'fields *;'


def parse_games() -> list:
    list_of_games = []
    response_games = requests.request("POST", f"https://api.igdb.com/v4/games", data=body_games, headers=headers)
    for game in response_games.json():
        try:
            list_of_games.append({
                "game_name": game.get("name", "alsdjf"),
                "summary": game["summary"],
                "twitch_url": game["url"]
            })
        except KeyError:
            continue

    return list_of_games

