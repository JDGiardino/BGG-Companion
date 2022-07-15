import unittest.mock
import pytest

from src.bgg_companion_game_filter import FilterBoardGames
from tests.models.TestBggCompanionGameFilterData import TestGameMatchesFilterData

# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestFilterGames:
    @staticmethod
    def test_default_filter_board_games():
        """Testing the default filter.  By default, without any other filter values, gameType is filtered for
        boardgames which removes any boardgame-expansion types."""
        test_data = TestGameMatchesFilterData()

        filtered_board_games = FilterBoardGames(board_games=test_data.board_games, game_filter=test_data.default_filter)
        actual_game_matches_filter = filtered_board_games.filter_games()
        expected_game_matches_filter = test_data.expected_default_filter

        assert actual_game_matches_filter == expected_game_matches_filter

    @staticmethod
    def test_minimum_maxplayers_filter():
        """Testing the filter for the minimum maxplayers amount a game should have.  If there are 4 players,
        the list should only contain games with a maxplayers of AT LEAST 4."""
        test_data = TestGameMatchesFilterData()

        filtered_board_games = FilterBoardGames(board_games=test_data.board_games,
                                                game_filter=test_data.minimum_maxplayers_filter)
        actual_game_matches_filter = filtered_board_games.filter_games()
        expected_game_matches_filter = test_data.expected_minimum_maxplayers_filter

        assert actual_game_matches_filter == expected_game_matches_filter

    @staticmethod
    def test_exact_players_filter():
        """Testing the filter for the exact players a game supports.  If there are 2 players, the list should only
        contain games that only support exactly 2 players."""
        test_data = TestGameMatchesFilterData()

        filtered_board_games = FilterBoardGames(board_games=test_data.board_games,
                                                game_filter=test_data.exact_players_filter)
        actual_exact_players_filter = filtered_board_games.filter_games()
        expected_exact_players_filter = test_data.expected_exact_players_filter

        assert actual_exact_players_filter == expected_exact_players_filter

