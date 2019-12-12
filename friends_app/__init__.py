import os
import random

from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


# fmt: off
from friends_app import db  # circular import case
# fmt: on


@app.route("/")
def index():
    episodes = db.get_db()
    chosen = random.choice(list(episodes.keys()))
    info = episodes[chosen]
    message = (
        f"Your episode for the current moment is {info['title']} "
        f"(season: {info['season']}, episode: {info['episode']})"
    )
    return message


if __name__ == "__main__":
    app.run(port=5000, debug=False, threaded=True)
