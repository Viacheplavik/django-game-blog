from typing import (
    List,
    Dict,
    Any
)

import requests


class IgdbWrapper:
    def __init__(self, client_id, secret_code):
        self.client_id = client_id
        self.secret_code = secret_code
        # TODO filters
        self.body_params = " fields *; "
        self._access_token = self._get_access_token()
        self.headers = self.create_header()

    def _get_access_token(self) -> str:
        token_response = requests.request("POST",
                                          f"https://id.twitch.tv/oauth2/token?"
                                          f"client_id={self.client_id}&"
                                          f"client_secret={self.secret_code}&"
                                          f"grant_type=client_credentials").json()
        access_token = token_response['access_token']
        return access_token

    def create_header(self) -> Dict[str, str]:
        header = {
            'Client-ID': self.client_id,
            'Authorization': f"Bearer {self._access_token}"
        }
        response_code = requests.request("POST",
                                         f"https://api.igdb.com/v4/games",
                                         data=self.body_params,
                                         headers=header
                                         ).status_code
        if response_code != 200:
            self._access_token = self._get_access_token()
            self.create_header()
        else:
            return {
                'Client-ID': self.client_id,
                'Authorization': f"Bearer {self._access_token}"
            }

    def get_games(self) -> List[Dict[str, Any]]:

        games_list = []
        response_games = requests.request("POST",
                                          f"https://api.igdb.com/v4/games",
                                          data=self.body_params,
                                          headers=self.headers
                                          )

        for game in response_games.json():
            games_list.append({
                "name": game.get("name", ''),
                "summary": game.get("summary", ''),
                "twitch_url": game.get("url", 'None')

            })
        return games_list



