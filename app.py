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
    make_response,
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
        resp = jsonify(dataclasses.asdict(random.choice(filtered_board_games)))
        resp.set_cookie("username", user)
        return resp
    except UserIsNoneError as exc:
        return abort(Response(response=str(exc), status=404))
    except Exception as exc:
        return abort(Response(response=str(exc), status=500))


@app.route("/page_visit_counter")
def page_visit_counter():
    count = int(request.cookies.get("visit-count", 0))
    count += 1
    message = f"You have visited BGG-Companion " + str(count) + " times!"

    resp = make_response(message)
    resp.set_cookie("visit-count", str(count))
    return resp


@app.route("/last_username")
def last_username():
    return request.cookies.get("username")


@app.route("/home")
def home():
    page_visit_counter()
    last_username()
    return render_template("home.html")
