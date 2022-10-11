import collections
import xmltodict
import logging

from logging import StreamHandler
from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter
from src.exceptions import UserIsNoneError, BoardGameIsNoneError, UserHasNoCollection
from src.bgg_companion_game_filter import FilterBoardGames
from src.bgg_companion_game_order import OrderBoardGames
from src.utils.requests_retry_client import RequestsRetryClient
from src.cache.DummyCache import DummyCache

from typing import OrderedDict

logger = logging.getLogger(__name__)


class BggCompanionApi(object):
    def __init__(self, request_client, cache):
        self.request_client = request_client
        self.cache = cache

    def request(self, url: str):
        response = self.request_client.request(method="GET", url=url)
        logging.info(f"Made a request to {url}")
        return response.text

    def get_collection(self, user: str) -> dict:
        cached_users_collection = self.cache.get(user)

        if cached_users_collection is not None:
            return cached_users_collection

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
        logging.info("Returning user's game collection")
        self.cache.set(user, users_game_collection)
        return users_game_collection

    def get_board_games(self, ids: tuple[str]) -> list[BoardGame]:
        cached_board_games = self.cache.get(ids)

        if cached_board_games is not None:
            return cached_board_games

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
        logging.info(f"All items assigned to the BoardGame class")
        self.cache.set(ids, board_games)
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
        logging.info("Returning id list")
        return id_list

    def get_users_board_games(self, user: str) -> list[BoardGame]:
        ids_list = self.get_users_game_ids(user)
        users_board_games = self.get_board_games(tuple(ids_list))
        logging.info("Returning user's board games list")
        return users_board_games

    def get_users_filtered_board_games(
        self, user: str, minplayers=None, maxplayers=None, playerrangetype=None
    ) -> list[BoardGame]:
        users_board_games = self.get_users_board_games(user)
        filtered_board_games = FilterBoardGames(
            board_games=users_board_games,
            game_filter=GameFilter(
                minplayers=minplayers, maxplayers=maxplayers, playerrangetype=playerrangetype
            ),
        )
        logging.info("Returning filtered board games")
        return filtered_board_games.filter_games()

    def get_users_ordered_board_games(self, user: str, order_by=None) -> list[BoardGame]:
        users_board_games = self.get_users_board_games(user)
        ordered_board_games = OrderBoardGames(
            board_games=users_board_games, order_by=order_by
        ).order_games()
        return ordered_board_games


# LEAVE BELOW COMMENTED : Used for development testing
if __name__ == "__main__":
#     bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient(), cache=None)
    print(f"__name__ is {__name__}")
