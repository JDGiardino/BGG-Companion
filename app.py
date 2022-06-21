import dataclasses
import random

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError
from src.utils.requests_retry_client import RequestsRetryClient

from flask import (
    Flask,
    request,
    Response,
    abort,
    jsonify,
    render_template,
)
from typing import Union

app = Flask(__name__)
# Run this by poetry run flask run


@app.route("/random_game")
def post_random_game_from_users_collection() -> Union[str, Response]:
    args = request.args
    user = args.get("user")
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())
    try:
        filtered_board_games = bgg_companion_api.get_users_filtered_board_games(user)
        return jsonify(dataclasses.asdict(random.choice(filtered_board_games)))
    except UserIsNoneError as exc:
        return abort(Response(response=str(exc), status=404))
    except Exception as exc:
        return abort(Response(response=str(exc), status=500))


@app.route("/home")
def home():
    return render_template("home.html")
