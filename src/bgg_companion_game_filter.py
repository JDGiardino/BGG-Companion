from src.models.BoardGame import BoardGame
from src.models.GameFilter import GameFilter


class FilterBoardGames:
    def __init__(self, board_games: list[BoardGame], game_filter: GameFilter):
        self.board_games = board_games
        self.game_filter = game_filter

    def filter_games(self) -> list[BoardGame]:
        filtered_board_games = []
        for game in self.board_games:
            if self.game_matches_filter(game):
                filtered_board_games.append(game)
        return filtered_board_games

    def game_matches_filter(self, game: BoardGame) -> bool:
        return (
            self.__game_type(game=game, gamefilter=self.game_filter)
            and self.__maxplayers_gt(game=game, gamefilter=self.game_filter)
            and self.__exactplayers(game=game, gamefilter=self.game_filter)
        )

    @staticmethod
    def __game_type(game: BoardGame, gamefilter: GameFilter) -> bool:
        return game.type == gamefilter.gameType

    @staticmethod
    def __maxplayers_gt(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.minimum_maxplayers is None or game.maxplayers >= gamefilter.minimum_maxplayers

    @staticmethod
    def __exactplayers(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.exactplayers is None or (
            game.maxplayers == gamefilter.exactplayers
            and game.minplayers == gamefilter.exactplayers
        )
