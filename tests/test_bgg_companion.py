import unittest.mock
import pytest

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError
from tests.models.TestBggCompanionVariables import (
    TestGetCollectionVariables,
    TestToBoardGameVariables,
)


# Tests are ran with poetry run pytest -vvvv or poetry run pytest -k test_function_name


class TestGetCollection(unittest.TestCase):
    @staticmethod
    def test_get_request_for_users_collection():
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
    def test_exception_for_invalid_user():
        """Testing the get_collection function for requesting a BGG collection of an invalid user"""

    test_variables = TestGetCollectionVariables()

    mock_response = unittest.mock.Mock(spec=["text"])
    mock_response.text = test_variables.invalid_user_response
    mock_request_client = unittest.mock.Mock(spec=["request"])
    mock_request_client.request.return_value = mock_response

    bgg_companion_api = BggCompanionApi(mock_request_client)
    with pytest.raises(UserIsNoneError):
        bgg_companion_api.get_collection("test__invalid_user")


class TestToBoardGame:
    @staticmethod
    def test_item_mapping_to_boardgame_THUMBNAIL_TRUE():
        """Testing the to_board_game function for mapping a given item that has a thumbnail to the BoardGame data
        class"""
        test_variables = TestToBoardGameVariables()

        bgg_companion_api = BggCompanionApi()
        test_item = test_variables.item_thumbnail_true
        test_boardgame = test_variables.boardgame_thumbnail_true

        actual_to_board_game = bgg_companion_api.to_board_game(test_item)
        expected_to_board_game = test_boardgame

        assert actual_to_board_game == expected_to_board_game

    @staticmethod
    def test_item_mapping_to_boardgame_THUMBNAIL_FALSE():
        """Testing the to_board_game function for mapping a given item that doesn't have a thumbnail to the BoardGame
        data class"""
        test_variables = TestToBoardGameVariables()

        bgg_companion_api = BggCompanionApi()
        test_item = test_variables.item_thumbnail_false
        test_boardgame = test_variables.boardgame_thumbnail_false

        actual_to_board_game = bgg_companion_api.to_board_game(test_item)
        expected_to_board_game = test_boardgame

        assert actual_to_board_game == expected_to_board_game

    @staticmethod
    def test_item_mapping_to_boardgame_NAME_IS_DICT():
        """Testing the to_board_game function for mapping a given item where the ["name"] value is a type OrderedDict
        to the BoardGame data class"""
        test_variables = TestToBoardGameVariables()

        bgg_companion_api = BggCompanionApi()
        test_item = test_variables.item_thumbnail_true
        test_boardgame = test_variables.boardgame_thumbnail_true

        actual_to_board_game = bgg_companion_api.to_board_game(test_item)
        expected_to_board_game = test_boardgame

        assert actual_to_board_game == expected_to_board_game

    @staticmethod
    def test_item_mapping_to_boardgame_NAME_IS_LIST():
        """Testing the to_board_game function for mapping a given item where the ["name"] value is a type list to the
        BoardGame data class"""
        test_variables = TestToBoardGameVariables()

        bgg_companion_api = BggCompanionApi()
        test_item = test_variables.item_thumbnail_false
        test_boardgame = test_variables.boardgame_thumbnail_false

        actual_to_board_game = bgg_companion_api.to_board_game(test_item)
        expected_to_board_game = test_boardgame

        assert actual_to_board_game == expected_to_board_game
