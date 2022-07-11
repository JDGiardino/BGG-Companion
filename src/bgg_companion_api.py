import collections
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
        string_xml = self.request(f"https://boardgamegeek.com/xmlapi2/collection?username={user}")
        xml_parse = xmltodict.parse(string_xml)
        if (
            "errors" in xml_parse
            and xml_parse["errors"]["error"]["message"] == "Invalid username specified"
        ):
            raise UserIsNoneError(
                "Invalid username specified.  Please enter a valid https://boardgamegeek.com/ username."
            )
        if xml_parse["items"]["@totalitems"] == "0":
            raise UserHasNoCollection("This user does not have a game collection on BoardGameGeek.")
        users_game_collection = xml_parse["items"]["item"]
        return users_game_collection

    @cached(cache=TTLCache(maxsize=500, ttl=300))
    def get_board_games(self, ids: tuple[str]) -> list[BoardGame]:
        string_xml = self.request(
            f'https://api.geekdo.com/xmlapi2/thing?id={",".join(ids)}&stats=1'
        )
        xml_parse = xmltodict.parse(string_xml)
        if "item" not in xml_parse["items"]:
            raise BoardGameIsNoneError(
                "There were no board games passed that exist within BoardGameGeek."
            )  # Exception is only raised when NONE of the ids can be found, and is not raised if 1+ ids can be found.
            # This shouldn't ever be raised since the ids are coming from get collection Board Game Geek API call.
        items = xml_parse["items"]["item"]
        if isinstance(items, OrderedDict):
            # If there is only a single game in the response make it a list as we expect later when iterating over items
            items = [items]
        board_games = []
        for item in items:
            board_games.append(self.__to_board_game(item))
        return board_games

    @staticmethod
    def __to_board_game(
        item: collections.OrderedDict,
    ) -> BoardGame:
        id = item["@id"]
        type = item["@type"]
        description = item["description"]
        minplayers = item["minplayers"]["@value"]
        maxplayers = item["maxplayers"]["@value"]
        yearpublished = item["yearpublished"]["@value"]
        averagerating = item["statistics"]["ratings"]["average"]["@value"]
        complexity = item["statistics"]["ratings"]["averageweight"]["@value"]
        if "thumbnail" in item and "image" in item:
            thumbnail = item["thumbnail"]
            image = item["image"]
        else:
            thumbnail = None
            image = None
        if isinstance(item["statistics"]["ratings"]["ranks"]["rank"], OrderedDict):
            overallrank = item["statistics"]["ratings"]["ranks"]["rank"]["@value"]
        elif isinstance(item["statistics"]["ratings"]["ranks"]["rank"], list):
            for a_dict in item["statistics"]["ratings"]["ranks"]["rank"]:
                if a_dict["@type"] == "subtype":
                    overallrank = a_dict["@value"]
                    break
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
            yearpublished=yearpublished,
            averagerating=averagerating,
            complexity=complexity,
            overallrank=overallrank,
            thumbnail=thumbnail,
            image=image,
        )

    def get_users_game_ids(self, user: str) -> list[str]:
        users_game_collection = self.get_collection(user)
        id_list = []
        for game in users_game_collection:
            id_list.append(game["@objectid"])
        return id_list

    def get_users_board_games(self, user: str) -> list[BoardGame]:
        ids_list = self.get_users_game_ids(user)
        users_board_games = self.get_board_games(tuple(ids_list))
        return users_board_games

    def get_users_filtered_board_games(
        self, user: str, maxplayers=None, exactplayers=None
    ) -> list[BoardGame]:
        users_board_games = self.get_users_board_games(user)
        filtered_board_games = FilterBoardGames(
            board_games=users_board_games,
            game_filter=GameFilter(maxplayers=maxplayers, exactplayers=exactplayers),
        )
        return filtered_board_games.filter_games()


# LEAVE BELOW COMMENTED : Used for development testing
# if __name__ == "__main__":
#     bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())
#     print(bgg_companion_api.get_users_filtered_board_games("JDGiardino"))
