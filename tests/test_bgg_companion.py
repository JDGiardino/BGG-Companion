import unittest.mock
import pytest

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError, UserHasNoCollection
from tests.models.TestBggCompanionVariables import (
    TestGetCollectionVariables,
    TestGetBoardGamesVariables,
)


# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestGetCollection(unittest.TestCase):
    @staticmethod
    def test_for_valid_user():
        """Testing the get_collection function for requesting a BGG collection of a valid user"""
        test_variables = TestGetCollectionVariables()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_variables.user_collection_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(mock_request_client)
        actual_get_collection = bgg_companion_api.get_collection("test_user")
        expected_get_collection = test_variables.expected_get_collection

        assert actual_get_collection == expected_get_collection

    @staticmethod
    def test_for_invalid_user():
        """Testing the get_collection function for requesting a BGG collection of an invalid user"""

        test_variables = TestGetCollectionVariables()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_variables.invalid_user_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(mock_request_client)
        with pytest.raises(UserIsNoneError):
            bgg_companion_api.get_collection("test_invalid_user")

    @staticmethod
    def test_for_valid_user_with_no_game_collection():
        """Testing the get_collection function for requesting a BGG collection of a valid user that does not have a game
         collection"""

        test_variables = TestGetCollectionVariables()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_variables.user_no_collection_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(mock_request_client)
        with pytest.raises(UserHasNoCollection):
            bgg_companion_api.get_collection("test_user_no_collection")


class TestGetBoardGames:
    @staticmethod
    def test_get_board_games_with_2_ids():
        test_variables = TestGetBoardGamesVariables()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_variables.two_ids_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(mock_request_client)
        actual_get_board_games = bgg_companion_api.get_board_games(tuple(['187645', '6902']))
        expected_get_board_games = test_variables.expected_two_ids

        assert actual_get_board_games == expected_get_board_games

    @staticmethod
    def test_get_board_games_with_1_id():
        test_variables = TestGetBoardGamesVariables()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_variables.one_id_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(mock_request_client)
        actual_get_board_games = bgg_companion_api.get_board_games(tuple(['6902']))
        expected_get_board_games = test_variables.expected_one_id

        assert actual_get_board_games == expected_get_board_games
