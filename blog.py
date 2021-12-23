from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import psql_login
from models import db
from models import app_user, blog_post, p_word
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = psql_login
db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/test", methods=["GET","POST"])
def test():
    if request.method == "GET":
        return render_template("signup.html")


# app.debug = True
# app.run(host='0.0.0.0', port=5000)
