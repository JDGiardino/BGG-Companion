import random
import xmltodict
from src.models.Game import Game
from src.exceptions import UserIsNoneError
from typing import Union
from src.utils.requests_retry_client import RequestsRetryClient
from cachetools import cached, TTLCache


def request(url: str):
    response = RequestsRetryClient().request(method='GET', url=url)
    return response.text


@cached(cache=TTLCache(maxsize=33, ttl=300))
def get_users_collection(user: str) -> Union[None, dict]:
    string_xml = request(f'https://boardgamegeek.com/xmlapi/collection/{user}?own=1')
    xml_parse = xmltodict.parse(string_xml)
    if "errors" in xml_parse and xml_parse["errors"]["error"]["message"] == "Invalid username specified":
        return None
    return xml_parse


def get_random_game(user: str) -> Game:
    xmldict = get_users_collection(user)
    if xmldict is None:
        raise UserIsNoneError("Invalid username specified.  Please enter a valid https://boardgamegeek.com/ username.")
    else:
        items = xmldict["items"]["item"]
        game_list = []
        for game in items:
            game_list.append(game["name"]["#text"])
        return Game(name=random.choice(game_list))
