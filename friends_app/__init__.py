import random
import os

from flask import Flask, render_template, send_from_directory
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
# this allows the css file to refresh instead of being cached and not resembling changes
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# fmt: off
from friends_app import db  # circular import case
# fmt: on


@app.route("/")
def index():
    episodes = db.get_db()
    chosen = random.choice(list(episodes.keys()))
    data = episodes[chosen]
    title = f"{data['title']}"
    season_episode = f"(season: {data['season']}, episode: {data['episode']})"
    image_id = f"s{data['season']}e{data['episode']}.jpg"
    description = data["description"]
    return render_template(
        "index.html",
        title=title,
        season_episode=season_episode,
        description=description,
        image_id=image_id
    )


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(port=5000, debug=False, threaded=True)
