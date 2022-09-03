import unittest.mock
import pytest

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError, UserHasNoCollection, BoardGameIsNoneError
from tests.models.TestBggCompanionApiData import (
    TestGetCollectionData,
    TestGetBoardGamesData,
)

from flask_caching import Cache
from flask import Flask
test_cache = Cache(config={"CACHE_NO_NULL_WARNING": True})
test_app = Flask(__name__)

test_cache.init_app(test_app)
# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestGetCollection:
    @staticmethod
    def test_for_valid_user():
        """Testing the get_collection function for requesting a BGG collection of a valid user"""
        test_data = TestGetCollectionData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.user_collection_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        actual_get_collection = bgg_companion_api.get_collection("test_user")
        expected_get_collection = test_data.expected_get_collection

        assert actual_get_collection == expected_get_collection

    @staticmethod
    def test_for_invalid_user():
        """Testing the get_collection function for requesting a BGG collection of an invalid user"""

        test_data = TestGetCollectionData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.invalid_user_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        with pytest.raises(UserIsNoneError):
            bgg_companion_api.get_collection("test_invalid_user")

    @staticmethod
    def test_for_valid_user_with_no_game_collection():
        """Testing the get_collection function for requesting a BGG collection of a valid user that does not have a game
        collection"""

        test_data = TestGetCollectionData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.user_no_collection_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        with pytest.raises(UserHasNoCollection):
            bgg_companion_api.get_collection("test_user_no_collection")


class TestGetBoardGames:
    @staticmethod
    def test_get_board_games_with_2_ids():
        """Testing the get_board_games function when 2 ids are passed in"""
        test_data = TestGetBoardGamesData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.two_ids_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        actual_get_board_games = bgg_companion_api.get_board_games(tuple(["187645", "6902"]))
        expected_get_board_games = test_data.expected_two_ids

        assert actual_get_board_games == expected_get_board_games

    @staticmethod
    def test_get_board_games_with_1_id():
        """Testing the get_board_games function when 1 id is passed in"""
        test_data = TestGetBoardGamesData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.one_id_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        actual_get_board_games = bgg_companion_api.get_board_games(tuple(["187645"]))
        expected_get_board_games = test_data.expected_one_id

        assert actual_get_board_games == expected_get_board_games

    @staticmethod
    def test_get_board_games_with_invalid_id():
        """Testing the get_board_games function when none of the ids passed in are valid in Board Game Geek"""
        test_data = TestGetBoardGamesData()

        mock_response = unittest.mock.Mock(spec=["text"])
        mock_response.text = test_data.invalid_id_response
        mock_request_client = unittest.mock.Mock(spec=["request"])
        mock_request_client.request.return_value = mock_response

        bgg_companion_api = BggCompanionApi(request_client=mock_request_client, cache=test_cache)
        with pytest.raises(BoardGameIsNoneError):
            bgg_companion_api.get_board_games(tuple(["111111111", "222222222"]))
