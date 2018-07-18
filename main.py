from flask import Flask, request, render_template, redirect, url_for, session
import os
import time
import threading
import bot
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Moppen(db.Model):
    __tablename__ = "moppen"

    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.Text)
    author = db.Column(db.Text)

    def __init__(self, joke, author):
        self.joke = joke
        self.author = author
    def __repr__(self):
        return  "{},{}".format(self.joke, self.author)

class Words(db.Model):
    __tablename__ = "words"

    woordenlijst = db.Column(db.Text, primary_key=True)

    def __init__(self, woordenlijst):
        self.wordenlijst = woordenlijst
    def __repr__(self):
        return  self.woordenlijst

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    mop = request.form.get("joke")
    auteur = request.form.get("name")
    words = "kanker kkr mogool mongool kut godverdomme bek reet lul kootzak eikel slet hoer www. www .nl porno"
    print(words)
    words = str(words)
    words = words.split(" ")
    print(words)
    if mop != "":
        badwords = 0
        for mopje in mop.split(" "):
            print(mopje)
            if mopje in words:
                badwords =+ 1
        for word in words:
            for mopje in mop.split(" "):
                if word in mopje:
                    badwords =+ 1
        print(badwords)
        if badwords < 1:
            mop = Moppen(mop, auteur)
            db.session.add(mop)
            db.session.commit()
            print("Toegevoegd!")
            print(Moppen.query.all())
    return "<meta http-equiv='refresh' content='0; url=/' />"

thread = threading.Thread(target=lambda: discordbot.run())
thread.start()

if __name__ == '__main__':
    global words
    app.run(port=10000, host="0.0.0.0")
