import dataclasses
import random


from src.bgg_companion_api import BggCompanionApi
from src.utils.serialize_to_json import SerializeToJson
from src.exceptions import UserIsNoneError, UserHasNoCollection
from src.utils.requests_retry_client import RequestsRetryClient
from src.forms.RandomGameForm import RandomGameForm

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
from flask_caching import Cache
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

config = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 600,  # 10 minutes
}

app = Flask(__name__)
app.config.from_mapping(config)

cache = Cache(app)

# Run this by poetry run flask run
USERNAME_COOKIE_NAME = "username"
VISIT_COUNT_COOKIE_NAME = "visit-count"


@app.route("/random_game")
def get_random_game_from_users_collection() -> Union[str, Response]:
    form = RandomGameForm(request.args)
    if form.validate():
        bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient(), cache=cache)
        try:
            filtered_board_games = bgg_companion_api.get_users_filtered_board_games(
                user=form.user.data,
                minplayers=form.minplayers.data,
                maxplayers=form.maxplayers.data,
                playerrangetype=form.playerrangetype.data,
                playstyle=form.playstyle.data,
                mincomplexity=form.mincomplexity.data,
                maxcomplexity=form.maxcomplexity.data,
            )
            resp = jsonify(dataclasses.asdict(random.choice(filtered_board_games)))
            app.logger.info(f"Random board game was selected")
            resp.set_cookie(key=USERNAME_COOKIE_NAME, value=form.user.data)
            app.logger.info(f"Cookie was set")
            return resp
        except UserIsNoneError as exc:
            app.logger.info(f"{form.user.data} does not exist within BoardGameGeek")
            return abort(Response(response=str(exc), status=404))
        except UserHasNoCollection as exc:
            app.logger.info(f"{form.user.data} does not have a board game collection")
            return abort(Response(response=str(exc), status=404))
        # TO DO: The below return should be removed to hide unhandled exceptions from users. Keeping for now for development
        except Exception as exc:
            return abort(Response(response=str(exc), status=500))
    else:
        error_message = ""
        for key, value in form.errors.items():
            error_message += (
                f"The following errors pertain to the {key} field:\n {','.join(value)}\n\n"
            )
        return abort(Response(response=error_message, status=400))


@app.route("/ordered_games")
def get_users_ordered_collection() -> Union[str, Response]:
    args = request.args
    user = args.get("user")
    order_by = args.get("orderby")
    if args.get("gametype") == "All":
        gametype = None
    else:
        gametype = args.get("gametype")
    if args.get("playstyle") == "All":
        playstyle = None
    else:
        playstyle = args.get("playstyle")
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient(), cache=cache)

    try:
        ordered_board_games = bgg_companion_api.get_users_ordered_board_games(
            user=user, order_by=order_by, playstyle=playstyle, gametype=gametype
        )
        app.logger.info(f"Board game collection has been ordered")
        resp = jsonify(SerializeToJson.serialize_ordered_board_games(ordered_board_games))
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


if __name__ == "__main__":
    app.run()
