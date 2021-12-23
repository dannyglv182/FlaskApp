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


@app.route("/signup", methods=["GET","POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        user_name = request.form["username"]
        hash_ = pbkdf2_sha256.hash(request.form["password"])

        # Create and store the new password object
        to_store = p_word(hash_value=hash_)
        db.session.add(to_store)
        db.session.commit()

        # Create and store the new user 
        to_store_2 = app_user(user_name=user_name, password=to_store.id)
        db.session.add(to_store_2)
        db.session.commit()
        return "Thank you."


app.debug = True
app.run(host='0.0.0.0', port=5000)
