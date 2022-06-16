import dataclasses

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
    send_from_directory,
)
from typing import Union

app = Flask(__name__, static_folder="frontend/build", static_url_path="/")
# Run this by poetry run flask run


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, "index.html")


@app.route("/random_game")
def post_random_game() -> Union[str, Response]:
    args = request.args
    user = args.get("user")
    bgg_companion_api = BggCompanionApi(request_client=RequestsRetryClient())
    try:
        return jsonify(dataclasses.asdict(bgg_companion_api.get_random_game(user)))
    except UserIsNoneError as exc:
        return abort(Response(response=str(exc), status=404))
    except Exception as exc:
        return abort(Response(response=str(exc), status=500))


@app.route("/home")
def home():
    return render_template("home.html")
