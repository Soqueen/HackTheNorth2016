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
            CREATE TABLE guests (
                id           BIGSERIAL      PRIMARY KEY,
                email        TEXT           NOT NULL,
                attending    BOOLEAN
            );
        """
    )

    db.query(
        """
            CREATE TABLE events (
                id           BIGSERIAL      PRIMARY KEY,
                guests_id    BIGSERIAL      REFERENCES guests(id),
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


def clear_db():
    """ Clear old database's tables
    """

    db.query(
        """
            DROP TABLE IF EXISTS events;
            DROP TABLE IF EXISTS guests;
        """
    )
