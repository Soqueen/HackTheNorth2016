# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

