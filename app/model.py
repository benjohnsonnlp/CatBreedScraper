from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class Kitty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    country = db.Column(db.String, unique=False, nullable=True)
    origin = db.Column(db.String, unique=False, nullable=True)
    body = db.Column(db.String, unique=False, nullable=True)
    coat = db.Column(db.String, unique=False, nullable=True)
    pattern = db.Column(db.String, unique=False, nullable=True)
    image_url = db.Column(db.String, unique=False, nullable=True)


if __name__ == '__main__':
    # db.create_all()