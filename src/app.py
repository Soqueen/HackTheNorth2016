# -*- coding: utf-8 -*-

import sys
import uuid
from flask import Flask, render_template, request
from api.database import insert_event, get_event_from_ref_id

app = Flask(__name__)
HOSTNAME = "www.eventplanner.com"
ref_id = None


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


@app.route('/send_invite', methods=('GET', 'POST'))
def send_invite():
    if request.method == 'POST':
        event_name = request.form["eventname"]
        event_location = request.form["eventlocation"]
        event_date = request.form["event_date"]
        event_start_time = request.form["eventstarttime"]
        event_end_time = request.form["eventendtime"]
        event_description = request.form["eventdescription"]
        event_host_name = request.form["username"]
        host_email = request.form["user_email"]

        global ref_id
        ref_id = generate_unique_url()

        print(ref_id, file=sys.stderr)

        insert_event(
            event_name,
            "{} {}".format(event_date, event_start_time),
            event_location,
            event_description,
            event_host_name,
            host_email,
            ref_id
        )

        return render_template("send_invite.html")
    return render_template("create.html")


@app.route('/share', methods=('GET', 'POST'))
# @app.route('/share/<ref_id>', methods=('GET', 'POST'))
def share():
    if request.method == 'POST':
        if ref_id:
            url = "{}/{}".format(HOSTNAME, ref_id)
            return render_template("share.html", url=url)
    return render_template("share.html")


@app.route('/planner/<ref_id>', methods=('GET', 'POST'))
def planner(ref_id):
    return render_template("planner.html")


@app.route('/split_budget', methods=('GET', 'POST'))
def split_budget():
    if request.method == 'POST':
        # place holder for rest api splitwise
        pass
    return render_template("split_budget.html")
@app.route('/bill_data')
def bill_data():
    #place holder to save bill name and value to DB
    return render_template("split_budget.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
