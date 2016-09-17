# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
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
        # placeholder for database
        # Grab info to store somewhere
        return render_template("invitation.html")
    return render_template("create.html")


@app.route('/invitation', methods=('GET', 'POST'))
def invitation():
    if request.method == 'POST':
        return render_template("finish.html")
    return render_template("invitation.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
