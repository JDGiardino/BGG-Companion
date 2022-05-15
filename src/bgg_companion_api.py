import collections
import random

import xmltodict
from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter
from src.exceptions import UserIsNoneError, BoardGameIsNoneError
from typing import Union, OrderedDict, Optional, Type
from src.utils.requests_retry_client import RequestsRetryClient
from cachetools import cached, TTLCache


def request(url: str):
    response = RequestsRetryClient().request(method='GET', url=url)
    return response.text


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_collection(user: str) -> Union[None, dict]:
    string_xml = request(f'https://boardgamegeek.com/xmlapi2/collection?username={user}')
    xml_parse = xmltodict.parse(string_xml)
    if "errors" in xml_parse and xml_parse["errors"]["error"]["message"] == "Invalid username specified":
        raise BoardGameIsNoneError("A board game was passed that does not exist within BoardGameGeek.")
    users_game_collection = xml_parse["items"]["item"]
    return users_game_collection


@cached(cache=TTLCache(maxsize=500, ttl=300))
def get_board_games(ids: tuple[str]) -> list[BoardGame]:
    string_xml = request(f'https://api.geekdo.com/xmlapi2/thing?id={",".join(ids)}')
    xml_parse = xmltodict.parse(string_xml)
    if "item" not in xml_parse["items"]:
        return []  # This returns when none of the given id(s) were found
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
    return BoardGame(id=id, name=name, description=description, type=type, minplayers=minplayers, maxplayers=maxplayers,
                     thumbnail=thumbnail, image=image)


def get_users_game_ids(user: str) -> list[str]:
    users_game_collection = get_collection(user)
    if users_game_collection is None:
        raise UserIsNoneError("Invalid username specified.  Please enter a valid https://boardgamegeek.com/ username.")
    else:
        id_list = []
        for game in users_game_collection:
            id_list.append(game["@objectid"])
        return id_list


def game_type(game: BoardGame, gamefilter: GameFilter) -> bool:
    return game.type == gamefilter.gameType


def maxplayers_gt(game: BoardGame, gamefilter: GameFilter) -> bool:
    return gamefilter.maxplayers is None or game.maxplayers >= gamefilter.maxplayers


def exactplayers(game: BoardGame, gamefilter: GameFilter) -> bool:
    return gamefilter.exactplayers is None or (game.maxplayers == gamefilter.exactplayers and game.minplayers == gamefilter.exactplayers)


def game_matches_filter(game: BoardGame, gamefilter: GameFilter) -> bool:
    return game_type(game=game, gamefilter=gamefilter) and \
           maxplayers_gt(game=game, gamefilter=gamefilter) and \
           exactplayers(game=game, gamefilter=gamefilter)


def filter_games(board_games: list[BoardGame], game_filter: GameFilter) -> list[BoardGame]:
    filtered_board_games = []
    for game in board_games:
        if game_matches_filter(game, game_filter):
            filtered_board_games.append(game)
    return filtered_board_games


def get_random_game(user: str, maxplayers=None, exactplayers=None) -> BoardGame:
    ids_list = get_users_game_ids(user)
    board_games = get_board_games(tuple(ids_list))
    game = random.choice(filter_games(board_games, GameFilter(maxplayers=maxplayers, exactplayers=exactplayers)))
    return game
