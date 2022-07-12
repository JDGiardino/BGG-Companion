from src.models.BoardGame import BoardGame


class OrderBoardGames:
    def __init__(self,  board_games: list[BoardGame], order_by: str):
        self.board_games = board_games
        self.order_by = order_by

    def order_games(self) -> list[BoardGame]:
        ordered_board_games = []
        if self.order_by == "rank":
            ordered_board_games = self.__order_by_rank(ordered_board_games)
            return ordered_board_games

    def __order_by_rank(self, ordered_board_games: list) -> list[BoardGame]:
        for game in self.board_games:
            if isinstance(game["overallrank"], float): # think through again, check if attribute is a float or always make it a float and look for -1 or obvious variable name for what is equal
                ordered_board_games.append(game)
        ordered_board_games.sort(key=lambda x: x.overallrank)
        return ordered_board_games
