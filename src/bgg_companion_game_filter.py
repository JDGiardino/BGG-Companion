from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter


class FilterBoardGame:

    def game_matches_filter(self, game: BoardGame, gamefilter: GameFilter) -> bool:
        return self.__game_type(game=game, gamefilter=gamefilter) and \
               self.__maxplayers_gt(game=game, gamefilter=gamefilter) and \
               self.__exactplayers(game=game, gamefilter=gamefilter)

    @staticmethod
    def __game_type(game: BoardGame, gamefilter: GameFilter) -> bool:
        return game.type == gamefilter.gameType

    @staticmethod
    def __maxplayers_gt(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.maxplayers is None or game.maxplayers >= gamefilter.maxplayers

    @staticmethod
    def __exactplayers(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.exactplayers is None or (game.maxplayers == gamefilter.exactplayers and game.minplayers == gamefilter.exactplayers)
