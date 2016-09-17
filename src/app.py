# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/create")
def create():
    return render_template("create.html")


@app.route('/save_data', methods=('GET', 'POST'))
def save_data():
    if request.method == 'POST':
        # placeholder for database
        # Grab info to store somewhere
        return render_template("event.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
