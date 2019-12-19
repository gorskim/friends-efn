import os
import re
import requests
import urllib

from bs4 import BeautifulSoup


FRIENDS_BASE_URL = "https://www.imdb.com/title/tt0108778/episodes?season="
NUMBER_OF_SEASONS = 10
IMAGE_DIR_BASE = "friends_app/static/images/episodes/"


def scrape_friends() -> dict:
    all_episodes = {}

    for num in range(NUMBER_OF_SEASONS):
        season = str(num + 1)
        response = requests.get(FRIENDS_BASE_URL + season)
        soup = BeautifulSoup(response.text, "html.parser")
        episodes = soup.findAll("div", {"class": "list_item odd"}) + soup.findAll(
            "div", {"class": "list_item even"}
        )

        for ep in episodes:
            id_raw = ep.find("div").text.replace("\n", "").strip()
            m = re.match(r"S(?P<season_nr>.*), Ep(?P<ep_nr>.*)$", id_raw)
            ep_nr = m.group("ep_nr")
            id = f"s{season}e{ep}"
            title, description = (
                ep.find("a", {"itemprop": "name"}).text.strip(),
                ep.find("div", {"class": "item_description"}).text.strip(),
            )
            image_url = ep.find("img", {"alt": title}).get("src").strip()
            id = f"s{season}e{ep_nr}"
            all_episodes[id] = {
                "season": season,
                "episode": ep_nr,
                "title": title,
                "description": description,
                "image_url": image_url,
            }
            # _download_image(image_url, f'{id}.jpg')

    return all_episodes


def _download_image(url: str, image_name: str):
    path = os.path.join(IMAGE_DIR_BASE + image_name)
    urllib.request.urlretrieve(url, path)
