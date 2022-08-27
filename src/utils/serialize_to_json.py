import math

from src.models.BoardGame import BoardGame


class SerializeToJson:
    @staticmethod
    def serialize_ordered_board_games(board_games: list[BoardGame]):
        json_ready_board_games = board_games
        for game in board_games:
            if game.overallrank == math.inf:
                object.__setattr__(game, "overallrank", None)
                # Games without a rank are set to infinity so that they can be ordered.  Here, we change ranks that are
                # infinity to None so that they can be used in JSON
        return json_ready_board_games
