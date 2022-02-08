from flask import Flask, request
from src.bgg_companion_api import get_random_game

app = Flask(__name__)
# Run this by poetry run flask run

@app.route("/random_game")
def post_random_game():
    args = request.args
    if args.get('user') is None:  # add exception handling for empty strings AND for rate limits
        user = 'JDGiardino'
    else:
        user = args.get('user')
    return get_random_game(user)  # return proper json rather than a string
