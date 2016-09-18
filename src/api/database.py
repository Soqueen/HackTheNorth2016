# -*- coding: utf-8 -*-

""" Database tool to interface wth PostGreSQL."""

import os
import yaml
from pg import DB

__author__ = "Edward Tran"
__version__ = "0.1.0"

config_file_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "config",
    "settings.yaml"
)

CONFIG = yaml.load(open(config_file_path))

# Create DB instance
db = DB(
    dbname=CONFIG["db"]["name"],
    host=CONFIG["db"]["host"],
    port=CONFIG["db"]["port"],
    user=CONFIG["db"]["user"],
    passwd=CONFIG["db"]["pw"]
)


def init_setup():
    """ Clean setup of the database.
    """

    clear_db()

    db.query(
        """
            CREATE TABLE events (
                id           BIGSERIAL      PRIMARY KEY,
                event_name   TEXT           NOT NULL,
                location     TEXT           NOT NULL,
                time         TIMESTAMP      NOT NULL,
                description  TEXT           ,
                host_name    TEXT           NOT NULL,
                email        TEXT           NOT NULL,
                url          TEXT           NOT NULL
            );
        """
    )

    db.query(
        """
            CREATE TABLE guests (
                id           BIGSERIAL      PRIMARY KEY,
                event_id     BIGSERIAL      REFERENCES events(id),
                email        TEXT           NOT NULL,
                attending    BOOLEAN
            );
        """
    )


def clear_db():
    """ Clear old database's tables
    """

    db.query(
        """
            DROP TABLE IF EXISTS guests;
            DROP TABLE IF EXISTS events;
        """
    )


def insert_event(event_name, time, location, description, host_name, email, url):
    """ Insert event data in the DB.

    Args:
        event_name (str): Name of the event.
        time (str): Time of the event.
        location (str): Location of the event.
        description (str): Description of the event.
        host_name (str): Host name.
        email (str): Email.
        url (str): Unique URL.
    """
    db.insert(
        "events",
        event_name=event_name,
        time=time,
        location=location,
        description=description,
        host_name=host_name,
        email=email,
        url=url
    )
    # import sys
    # print(is_url_unique(url), file=sys.stderr)

# TODO: NOT DONE
def is_url_unique(url):
    count = db.query(
        """
            SELECT COUNT(event_name)
            FROM events
            WHERE url = '{}'
        """.format(url)
    )
    # print(count)

if __name__ == '__main__':
    init_setup()
