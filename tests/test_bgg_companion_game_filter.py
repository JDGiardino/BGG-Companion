import unittest.mock
import pytest

from src.bgg_companion_game_filter import FilterBoardGames
from tests.models.TestBggCompanionGameFilterData import TestFilterGamesData

# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestFilterGames:
    @staticmethod
    def test_default_filter_board_games():
        """Testing the default filter.  By default, without any other filter values, gameType is filtered for
        boardgames which removes any boardgame-expansion types."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.default_filter
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.expected_default_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_minplayers_in_range_filter_01():
        """Testing in-range filter for minimum players.  Example : If a (1 min - 4 max) player range is specified,
        games with a (2 min - 4 max) player range will not be present in the BoardGame list.
        Because if you only had 1 player, they could not play the 2 minimum players game therefore it's out of range."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.minplayers_in_range_filter_01
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.expected_minplayers_in_range_filter_list_01

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_minplayers_in_range_filter_02():
        """Testing in-range filter for minimum players.  Example : If a (2 min - 4 max) player range is specified,
        games with a (1 min - 4 max) player range will be present in the BoardGame list.
        Because if you only had 2 players, they could still play the 1 minimum players game therefore it's in range."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.minplayers_in_range_filter_02
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.expected_minplayers_in_range_filter_list_02

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_maxplayers_in_range_filter_01():
        """Testing in-range for maximum players.  Example: If a (1 min - 5 max) player range is specified,
        games with a (1 min - 4 max) player range will not be present in the BoardGame list.
        Because if you have 5 players total, they could not play the 4 maximum player game therefore it's out of range."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.maxplayers_in_range_filter_01
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.expected_maxplayers_in_range_filter_list_01

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_maxplayers_in_range_filter_02():
        """Testing in-range for maximum players.  Example: If a (1 min - 4 max) player range is specified,
        games with a (1 min - 5 max) player range will be present in the BoardGame list.
        Because if you have 4 players total, they could still play the 5 maximum player game therefore it's in range."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.maxplayers_in_range_filter_02
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.expected_maxplayers_in_range_filter_list_02

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_minplayers_exact_filter():
        """Testing exact range filter for minimum players.  Example : If 2 minimum players is specified,
        games with 1 minimum players will not be present in the BoardGame list.
        Because the game's range needs to match the filtered range exactly"""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.minplayers_exact_filter
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.minplayers_exact_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_maxplayers_exact_filter():
        """Testing exact range filter for maximum players.  Example : If 4 maximum players is specified,
        games with 3 maximum players will not be present in the BoardGame list.
        Because the game's range needs to match the filtered range exactly"""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.maxplayers_exact_filter
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.maxplayers_exact_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_playstyle_filter_01():
        """Testing when playstyle is set to cooperative in the game filter."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.playstyle_cooperative_filter
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.playstyle_cooperative_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_playstyle_filter_02():
        """Testing when playstyle is set to competitive in the game filter."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games, game_filter=test_data.playstyle_competitive_filter
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.playstyle_competitive_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games

    @staticmethod
    def test_gametype_filter():
        """Testing when gametype is set to boardgameexpansion in the game filter."""
        test_data = TestFilterGamesData()

        filtered_board_games = FilterBoardGames(
            board_games=test_data.board_games,
            game_filter=test_data.gametype_boardgameexpansion_filter,
        )
        actual_filtered_board_games = filtered_board_games.filter_games()
        expected_filtered_board_games = test_data.gametype_boardgameexpansion_filter_list

        assert actual_filtered_board_games == expected_filtered_board_games
