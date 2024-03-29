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
            self.__gametype(game=game)
            and self.__player_range_type(game=game)
            and self.__playstyle_type(game=game)
            and self.__complexity_range(game=game)
        )

    def __gametype(self, game: BoardGame) -> bool:
        return self.game_filter.gametype is None or game.type == self.game_filter.gametype

    def __player_range_type(self, game: BoardGame) -> bool:
        if self.game_filter.playerrangetype == "normal":
            return self.__minplayers_in_range(
                game=game, gamefilter=self.game_filter
            ) and self.__maxplayers_in_range(game=game, gamefilter=self.game_filter)
        elif self.game_filter.playerrangetype == "exact":
            return self.__minplayers_exact(
                game=game, gamefilter=self.game_filter
            ) and self.__maxplayers_exact(game=game, gamefilter=self.game_filter)
        else:
            return True

    def __playstyle_type(self, game: BoardGame) -> bool:
        return self.game_filter.playstyle is None or self.game_filter.playstyle == game.playstyle

    def __complexity_range(self, game: BoardGame) -> bool:
        return self.__mincomplexity_in_range(
            game=game, gamefilter=self.game_filter
        ) and self.__maxcomplexity_in_range(game=game, gamefilter=self.game_filter)

    @staticmethod
    def __minplayers_in_range(game: BoardGame, gamefilter: GameFilter) -> bool:
        return (
            gamefilter.minplayers is None
            or game.maxplayers >= gamefilter.minplayers >= game.minplayers
        )

    @staticmethod
    def __maxplayers_in_range(game: BoardGame, gamefilter: GameFilter) -> bool:
        return (
            gamefilter.maxplayers is None
            or game.maxplayers >= gamefilter.maxplayers >= game.minplayers
        )

    @staticmethod
    def __minplayers_exact(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.minplayers is None or game.minplayers == gamefilter.minplayers

    @staticmethod
    def __maxplayers_exact(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.maxplayers is None or game.maxplayers == gamefilter.maxplayers

    @staticmethod
    def __mincomplexity_in_range(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.mincomplexity is None or game.complexity >= gamefilter.mincomplexity

    @staticmethod
    def __maxcomplexity_in_range(game: BoardGame, gamefilter: GameFilter) -> bool:
        return gamefilter.maxcomplexity is None or game.complexity <= gamefilter.maxcomplexity
