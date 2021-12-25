from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import psql_login

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = psql_login
db = SQLAlchemy(app)

class app_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.Integer, 
                         db.ForeignKey("p_word.id"),
                         unique=True,
                         nullable=False)

class blog_post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer, db.ForeignKey("app_user.id"), nullable=False)
    text = db.Column(db.String(140), nullable=False)


class p_word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash_value = db.Column(db.String(140), nullable=False)


db.create_all()
