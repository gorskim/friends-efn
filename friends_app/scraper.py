import time
import urllib.request

import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/List_of_Friends_episodes"


def scrape_friends():
    all_episodes = {}
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.findAll(
        "table", {"class": "wikitable plainrowheaders wikiepisodetable"}
    )
    for i, table in enumerate(tables):
        season = str(i + 1)
        episodes = table.findAll("tr", {"class": "vevent"})
        for episode in episodes:
            ep_id_raw, title = (
                str(episode.find("td").text),
                episode.find("td", {"class": "summary"}).text,
            )
            ep = ep_id_raw if len(ep_id_raw) <= 2 else ep_id_raw[:2]
            id = f"s{season}e{ep}"
            all_episodes[id] = {
                "season": season,
                "episode": ep,
                "title": title,
                "image_path": "",
            }
    return all_episodes
