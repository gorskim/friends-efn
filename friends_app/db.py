import shelve

from flask import g
import logging
from friends_app.scraper import scrape_friends
from friends_app import app


log = logging.getLogger(__name__)


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        log.info("Creating new db...")
        db = g._database = shelve.open("friends.db", writeback=True)
        if not db.keys():
            log.info("Scraping...")
            try:
                episodes = scrape_friends()
                log.info("Scrapping finished successfully")
                for id, info in episodes.items():
                    db[id] = info
            except:
                log.exception("Scrapping failed.")
        return db


@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, "_database", None)
    if db:
        db.close()
