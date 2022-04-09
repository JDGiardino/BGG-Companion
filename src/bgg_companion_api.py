import collections
import random
import xmltodict
from src.models.BoardGame import BoardGame
from src.exceptions import UserIsNoneError
from typing import Union, OrderedDict
from src.utils.requests_retry_client import RequestsRetryClient
from cachetools import cached, TTLCache


def request(url: str):
    response = RequestsRetryClient().request(method='GET', url=url)
    return response.text


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_users_collection(user: str) -> Union[None, dict]:
    string_xml = request(f'https://boardgamegeek.com/xmlapi2/collection?username={user}')
    xml_parse = xmltodict.parse(string_xml)
    if "errors" in xml_parse and xml_parse["errors"]["error"]["message"] == "Invalid username specified":
        return None
    return xml_parse


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_board_games(board_game_id: str) -> list[BoardGame]:
    string_xml = request(f'https://api.geekdo.com/xmlapi2/thing?id={board_game_id}')
    xml_parse = xmltodict.parse(string_xml)
    items = xml_parse["items"]["item"]
    board_games = []
    for item in items:
        board_games.append(__to_board_game(item))
    return board_games


def __to_board_game(item: collections.OrderedDict) -> BoardGame:
    id = item["@id"]
    type = item["@type"]
    description = item["description"]
    minplayers = item["minplayers"]["@value"]
    maxplayers = item["maxplayers"]["@value"]
    thumbnail = item["thumbnail"]
    image = item["image"]
    if isinstance(item["name"], OrderedDict):
        name = item["name"]["@value"]
    elif isinstance(item["name"], list):
        for a_dict in item["name"]:
            if a_dict["@type"] == "primary":
                name = a_dict["@value"]
    else:
        name = None
    return BoardGame(id=id, name=name, description=description, type=type, minplayers=minplayers, maxplayers=maxplayers,
                     thumbnail=thumbnail, image=image)


def get_object_ids(user: str) -> list[str]:
    xmldict = get_users_collection(user)
    if xmldict is None:
        raise UserIsNoneError("Invalid username specified.  Please enter a valid https://boardgamegeek.com/ username.")
    else:
        items = xmldict["items"]["item"]
        id_list = []
        for item in items:
            id_list.append(item["@objectid"])
        return id_list


def get_random_game(user: str) -> Union[BoardGame, UserIsNoneError]:
    try:
        id_list = get_object_ids(user)
    except UserIsNoneError as exc:
        return exc
    id_string = ",".join(id_list)
    board_games = get_board_games(id_string)
    for game in board_games:
        if game.type != "boardgame":
            board_games.remove(game)
    game = random.choice(board_games)
    return game
