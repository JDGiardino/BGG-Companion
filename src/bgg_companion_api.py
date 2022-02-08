import random
from xml.dom import minidom
from src.utils.requests_retry_client import RequestsRetryClient


def request(url: str):
    response = RequestsRetryClient().request(method='GET', url=url)
    return response.text


def get_users_collection(user):
    string_xml = request(f'https://boardgamegeek.com/xmlapi/collection/{user}?own=1')
    xmlparse = minidom.parseString(string_xml)
    return xmlparse


def get_random_game(user):
    xmlparse = get_users_collection(user)  # add caching for this
    games = xmlparse.getElementsByTagName("name")
    game_list = []
    for game in games:
        game_list.append(game.firstChild.nodeValue)
    return random.choice(game_list)
