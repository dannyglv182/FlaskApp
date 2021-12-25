from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import psql_login
from models import db
from models import app_user, blog_post, p_word
from passlib.hash import pbkdf2_sha256
from db_functions import insert_new_password, insert_new_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = psql_login
db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/signup", methods=["GET","POST"])
def sign_up():
    """ GET and POST for signing up.

    GET request renders the sign up template

    POST request inserts the new user and password's hash value into 
    the database.
    """
    if request.method == "GET":
        return render_template("signup.html")
    else:
        user_name = request.form["username"]
        hash_ = pbkdf2_sha256.hash(request.form["password"])

        # Insert the new password object and store it in password_to_store
        password_to_store = insert_new_password(hash_) 

        # Insert the new user
        user_to_store = insert_new_user(user_name, password_to_store.id) 
        return "Thank you."


@app.route("/login", methods=["GET","POST"])
def log_in():
    """ GET and POST for logging in.

    GET request renders the sign up template

    POST request uses passlib to verify the inputted password with the hash
    value stored in the database. If pbkdf2_sha256.verify() returns true, the
    user is logged in.
    """
    if request.method == "GET":
        return render_template("signup.html")
    else:
        try:

            # Gather username and password from the request response
            user_name = request.form["username"]
            password = request.form["password"]
            user_obj = app_user.query.filter_by(user_name=user_name).one()
            password_obj = p_word.query.filter_by(id=user_obj.password).one()

            # Verify that the password is correct using Passlib
            hash_comparison = pbkdf2_sha256.verify(password, password_obj.hash_value)            
        except:
            return "Exception"

        # hash_comparison is true if the password is correct
        if hash_comparison == True:
            return "Thank you for logging in."
        else:
            return "Sorry. Try again."


app.debug = True
app.run(host='0.0.0.0', port=5000)
