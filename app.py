import dataclasses
from flask import Flask, request, Response, abort, jsonify, render_template
from typing import Union
from src.bgg_companion_api import get_random_game

app = Flask(__name__)
# Run this by poetry run flask run


@app.route("/random_game")
def post_random_game() -> Union[str, Response]:
    args = request.args
    user = args.get('user')
    try:
        return jsonify(dataclasses.asdict(get_random_game(user)))
    except Exception as exc:
        return abort(Response(response=str(exc), status=404))


@app.route("/home")
def home():
    return render_template("home.html")
