import dataclasses
import random

from src.bgg_companion_api import BggCompanionApi
from src.exceptions import UserIsNoneError, UserHasNoCollection
from src.utils.requests_retry_client import (
    RequestsRetryClient,
    make_retry_strategy,
    DEFAULT_HTTP_RETRY_CODES,
)
from logging.config import dictConfig
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

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
# Run this by poetry run flask run
USERNAME_COOKIE_NAME = "username"
VISIT_COUNT_COOKIE_NAME = "visit-count"


@app.route("/random_game")
def get_random_game_from_users_collection() -> Union[str, Response]:
    args = request.args
    user = args.get("user")
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())

    try:
        filtered_board_games = bgg_companion_api.get_users_filtered_board_games(user)
        app.logger.info(f"Random board game was selected")
        resp = jsonify(dataclasses.asdict(random.choice(filtered_board_games)))
        resp.set_cookie(key=USERNAME_COOKIE_NAME, value=user)
        app.logger.info(f"Cookie was set")
        return resp
    except UserIsNoneError as exc:
        app.logger.info(f"{user} does not exist within BoardGameGeek")
        return abort(Response(response=str(exc), status=404))
    except UserHasNoCollection as exc:
        app.logger.info(f"{user} does not have a board game collection")
        return abort(Response(response=str(exc), status=404))
    # TO DO: The below return should be removed to hide unhandled exceptions from users. Keeping for now for development
    except Exception as exc:
        app.logger.info(f"Uh oh error called {exc} happened")
        return abort(Response(response=str(exc), status=500))


@app.route("/all_games")
def get_all_games_from_users_collection() -> Union[str, Response]:
    args = request.args
    user = args.get("user")
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())

    try:
        board_games = bgg_companion_api.get_users_board_games(user)
        app.logger.info(f"Board game collection has been ordered")
        resp = jsonify(board_games)
        resp.set_cookie(key=USERNAME_COOKIE_NAME, value=user)
        return resp
    except UserIsNoneError as exc:
        app.logger.info(f"{user} does not exist within BoardGameGeek")
        return abort(Response(response=str(exc), status=404))
    except UserHasNoCollection as exc:
        app.logger.info(f"{user} does not have a board game collection")
        return abort(Response(response=str(exc), status=404))
    # TO DO: The below return should be removed to hide unhandled exceptions from users. Keeping for now for development
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


@app.route("/collection")
def collection():
    return render_template("collection.html")
