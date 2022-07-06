import dataclasses
import random

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError
from src.utils.requests_retry_client import RequestsRetryClient, make_retry_strategy, DEFAULT_HTTP_RETRY_CODES

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
USERNAME_COOKIE_NAME = "username"
VISIT_COUNT_COOKIE_NAME = "visit-count"


@app.route("/random_game")
def post_random_game_from_users_collection() -> Union[str, Response]:
    args = request.args
    user = args.get("user")

    # BGG's API usually responds with a 202 and retrying gets the 200
    retry_codes = list(DEFAULT_HTTP_RETRY_CODES) + [202]
    retry = make_retry_strategy(retry_codes=retry_codes)
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient(retry_strategy=retry))

    try:
        filtered_board_games = bgg_companion_api.get_users_filtered_board_games(user)
        resp = jsonify(dataclasses.asdict(random.choice(filtered_board_games)))
        resp.set_cookie(key=USERNAME_COOKIE_NAME, value=user)
        return resp
    except UserIsNoneError as exc:
        return abort(Response(response=str(exc), status=404))
    except Exception as exc:
        return abort(Response(response=str(exc), status=500))


@app.route("/page_visit_counter")
def page_visit_counter():
    count = int(request.cookies.get(VISIT_COUNT_COOKIE_NAME, 0))
    count += 1
    message = f"Recently, you've visited BGG-Companion " + str(count) + " times!"

    resp = make_response(message)
    resp.set_cookie(key=VISIT_COUNT_COOKIE_NAME, value=str(count))
    return resp


@app.route("/last_username")
def last_username():
    return request.cookies.get(USERNAME_COOKIE_NAME, "")


@app.route("/home")
def home():
    return render_template("home.html")
