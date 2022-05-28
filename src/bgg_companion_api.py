import collections
import random
import xmltodict

from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter
from src.exceptions import UserIsNoneError, BoardGameIsNoneError
from src.utils.requests_retry_client import RequestsRetryClient
from src.bgg_companion_game_filter import FilterBoardGames

from typing import Union, OrderedDict
from cachetools import cached, TTLCache


def request(url: str):
    response = RequestsRetryClient().request(method="GET", url=url)
    return response.text


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_users_collection(user: str) -> Union[None, dict]:
    string_xml = request(
        f"https://boardgamegeek.com/xmlapi2/collection?username={user}"
    )
    xml_parse = xmltodict.parse(string_xml)
    if (
        "errors" in xml_parse
        and xml_parse["errors"]["error"]["message"] == "Invalid username specified"
    ):
        return None
    users_game_collection = xml_parse["items"]["item"]
    return users_game_collection


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_board_games(ids: tuple[str]) -> list[BoardGame]:
    string_xml = request(f'https://api.geekdo.com/xmlapi2/thing?id={",".join(ids)}')

    xml_parse = xmltodict.parse(string_xml)
    if "item" not in xml_parse["items"]:
        raise BoardGameIsNoneError("A board game was passed that does not exist within BoardGameGeek.")
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
    if "thumbnail" in item and "image" in item:
        thumbnail = item["thumbnail"]
        image = item["image"]
    else:
        thumbnail = None
        image = None
    if isinstance(item["name"], OrderedDict):
        name = item["name"]["@value"]
    elif isinstance(item["name"], list):
        for a_dict in item["name"]:
            if a_dict["@type"] == "primary":
                name = a_dict["@value"]
                break
    else:
        name = None
    return BoardGame(
        id=id,
        name=name,
        description=description,
        type=type,
        minplayers=minplayers,
        maxplayers=maxplayers,
        thumbnail=thumbnail,
        image=image,
    )


def get_users_game_ids(user: str) -> list[str]:
    users_game_collection = get_collection(user)
    id_list = []
    for game in users_game_collection:
        id_list.append(game["@objectid"])
    return id_list


def get_random_game(user: str, maxplayers=None, exactplayers=None) -> BoardGame:
    ids_list = get_users_game_ids(user)
    board_games = get_board_games(tuple(ids_list))
    game_filter = GameFilter(maxplayers=maxplayers, exactplayers=exactplayers)
    filtered_board_games = FilterBoardGames(board_games=board_games, game_filter=game_filter)
    game = random.choice(filtered_board_games.filter_games())
    return game
