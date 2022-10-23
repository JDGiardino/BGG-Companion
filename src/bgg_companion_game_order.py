import copy

from src.models.BoardGame import BoardGame


class OrderBoardGames:
    ORDER_BY_ALPHABET = "alphabet"
    ORDER_BY_RANK = "rank"
    ORDER_BY_RATING = "rating"
    ORDER_BY_COMPLEXITY = "complexity"

    def __init__(self, board_games: list[BoardGame], order_by: str):
        self.board_games = board_games
        self.order_by = order_by

    def order_games(self) -> list[BoardGame]:
        ordered_board_games = copy.deepcopy(self.board_games)
        if self.order_by == self.ORDER_BY_RANK:
            ordered_board_games.sort(key=lambda x: x.overallrank)
        elif self.order_by == self.ORDER_BY_RATING:
            ordered_board_games.sort(key=lambda x: x.averagerating, reverse=True)
        elif self.order_by == self.ORDER_BY_COMPLEXITY:
            ordered_board_games.sort(key=lambda x: x.complexity, reverse=True)
        else:
            ordered_board_games.sort(key=lambda x: x.name)
        return ordered_board_games
