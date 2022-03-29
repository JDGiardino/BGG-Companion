import requests

print("Hello please enter a username to get a random game")
user = input("> ")


def get_random_game():
    game = requests.get(url=f'http://127.0.0.1:5000/random_game?user={user}')
    print(game.text)


if __name__ == "__main__":
    get_random_game("JDGiardino")
