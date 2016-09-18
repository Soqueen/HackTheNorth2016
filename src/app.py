# -*- coding: utf-8 -*-

import sys
import uuid
from flask import Flask, render_template, request
from api.database import insert_event

app = Flask(__name__)


def generate_unique_url():
    """ Generator Unique URL."""
    return str(uuid.uuid4())[:11].replace("-", "").lower()


@app.route("/")
def home():
    # print("HI", file=sys.stderr)
    return render_template("base.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/create")
def create():
    return render_template("create.html")


@app.route('/save_general', methods=('GET', 'POST'))
def save_data():
    if request.method == 'POST':
        event_name = request.form["eventname"]
        event_location = request.form["eventlocation"]
        event_date = request.form["event_date"]
        event_start_time = request.form["eventstarttime"]
        event_end_time = request.form["eventendtime"]
        event_description = request.form["eventdescription"]
        event_host_name = request.form["username"]
        host_email = request.form["user_email"]

        url_ref = generate_unique_url()

        insert_event(
            event_name,
            "{} {}".format(event_date, event_start_time),
            event_location,
            event_description,
            event_host_name,
            host_email,
            url_ref
        )

        return render_template("invitation.html")
    return render_template("create.html")


@app.route('/invitation', methods=('GET', 'POST'))
def invitation():
    if request.method == 'POST':
        return render_template("finish.html")
    return render_template("invitation.html")

@app.route('/split_budget', methods=('GET', 'POST'))
def split_budget():
    if request.method == 'POST':
        # place holder for rest api splitwise
        pass
    return render_template("split_budget.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
