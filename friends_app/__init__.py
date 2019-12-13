import os
import random

from flask import Flask, render_template
from flask_restful import Api



app = Flask(__name__)
api = Api(app)
# this allows the css file to refresh instead of being cached and not resembling changes
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(port=5000, debug=False, threaded=True)
