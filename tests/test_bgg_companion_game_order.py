import unittest.mock
import pytest

from src.bgg_companion_game_order import OrderBoardGames
from tests.models.TestBggCompanionGameOrderData import TestOrderGamesData

# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestOrderGames:
    @staticmethod
    def test_order_games_by_alphabet():
        """Testing ordering a board game collection alphabetically."""
        test_data = TestOrderGamesData()

        ordered_board_games = OrderBoardGames(
            board_games=test_data.board_games, order_by="alphabet"
        )
        actual_order_games = ordered_board_games.order_games()
        expected_order_games = test_data.expected_order_games_by_alphabet

        assert actual_order_games == expected_order_games

    @staticmethod
    def test_order_games_by_rank():
        """Testing ordering a board game collection by their rank."""
        test_data = TestOrderGamesData()

        ordered_board_games = OrderBoardGames(board_games=test_data.board_games, order_by="rank")
        actual_order_games = ordered_board_games.order_games()
        expected_order_games = test_data.expected_order_games_by_rank

        assert actual_order_games == expected_order_games

    @staticmethod
    def test_order_games_by_rating():
        """Testing ordering a board game collection by their rating."""
        test_data = TestOrderGamesData()

        ordered_board_games = OrderBoardGames(board_games=test_data.board_games, order_by="rating")
        actual_order_games = ordered_board_games.order_games()
        expected_order_games = test_data.expected_order_games_by_rating

        assert actual_order_games == expected_order_games

    @staticmethod
    def test_order_games_by_complexity():
        """Testing ordering a board game collection by their complexity."""
        test_data = TestOrderGamesData()

        ordered_board_games = OrderBoardGames(
            board_games=test_data.board_games, order_by="complexity"
        )
        actual_order_games = ordered_board_games.order_games()
        expected_order_games = test_data.expected_order_games_by_complexity

        assert actual_order_games == expected_order_games
