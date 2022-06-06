import collections
import random
import xmltodict

from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter
from src.exceptions import UserIsNoneError, BoardGameIsNoneError, UserHasNoCollection
from src.utils.requests_retry_client import RequestsRetryClient
from src.bgg_companion_game_filter import FilterBoardGames

from typing import OrderedDict
from cachetools import cached, TTLCache


class BggCompanionApi(object):
    def __init__(self, request_client):
        self.request_client = request_client

    def request(self, url: str):
        response = self.request_client.request(method="GET", url=url)
        return response.text

    @cached(cache=TTLCache(maxsize=500, ttl=300))
    def get_collection(self, user: str) -> dict:
        string_xml = self.request(
            f"https://boardgamegeek.com/xmlapi2/collection?username={user}"
        )
        xml_parse = xmltodict.parse(string_xml)
        if (
            "errors" in xml_parse
            and xml_parse["errors"]["error"]["message"] == "Invalid username specified"
        ):
            raise UserIsNoneError(
                "Invalid username specified.  Please enter a valid https://boardgamegeek.com/ username."
            )
        if xml_parse["items"]["@totalitems"] == "0":
            raise UserHasNoCollection(
                "This user does not have a game collection on BoardGameGeek."
            )
        users_game_collection = xml_parse["items"]["item"]
        return users_game_collection

    @cached(cache=TTLCache(maxsize=500, ttl=300))
    # testing this should be how many ids passed vs how many board games were in the list.  id doesn't exist error, 2 ids 2 games. no ids no games. 1 id 1 games.  exception is raised only if all ids are not exists and this is not obvious so should be a rtesrt.  why is behavior different. 1 real 1 not
    def get_board_games(self, ids: tuple[str]) -> list[BoardGame]:
        string_xml = self.request(
            f'https://api.geekdo.com/xmlapi2/thing?id={",".join(ids)}'
        )
        xml_parse = xmltodict.parse(string_xml)
        if "item" not in xml_parse["items"]:
            raise BoardGameIsNoneError(
                "A board game was passed that does not exist within BoardGameGeek."
            )
        items = xml_parse["items"]["item"]
        board_games = []
        for item in items:
            board_games.append(self.to_board_game(item))
        return board_games

    @staticmethod
    def to_board_game(item: collections.OrderedDict) -> BoardGame: # make this priavte again and only test its caller
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

    def get_users_game_ids(self, user: str) -> list[str]:
        users_game_collection = self.get_collection(user)
        id_list = []
        for game in users_game_collection:
            id_list.append(game["@objectid"])
        return id_list

    def get_random_game(
        self, user: str, maxplayers=None, exactplayers=None
    ) -> BoardGame:
        ids_list = self.get_users_game_ids(user)
        board_games = self.get_board_games(tuple(ids_list))
        game_filter = GameFilter(maxplayers=maxplayers, exactplayers=exactplayers)
        filtered_board_games = FilterBoardGames(
            board_games=board_games, game_filter=game_filter
        )
        game = random.choice(filtered_board_games.filter_games())
        return game


# LEAVE BELOW COMMENTED : Used for development testing
if __name__ == "__main__":
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())
    print(bgg_companion_api.get_random_game("omaryahir"))
