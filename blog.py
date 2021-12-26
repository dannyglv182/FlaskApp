from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from flask_sqlalchemy import SQLAlchemy
from config import psql_login, secret_key
from models import db
from models import app_user, blog_post, p_word
from passlib.hash import pbkdf2_sha256
from db_functions import insert_new_password, insert_new_user
from db_functions import username_exists, insert_new_post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = psql_login
app.secret_key = secret_key
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

    user_name = request.form["username"]
    hash_ = pbkdf2_sha256.hash(request.form["password"])

    # Check if the username already exists and return instead of moving on
    if username_exists(user_name) == True:
        return "Sorry that username is taken."

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

    # Request is a Post request
    try:

        # Gather username and password from the request response
        user_name = request.form["username"]
        password = request.form["password"]
        user_obj = app_user.query.filter_by(user_name=user_name).one()
        password_obj = p_word.query.filter_by(id=user_obj.password).one()

        # Verify that the password is correct using Passlib
        hash_comparison = pbkdf2_sha256.verify(password, password_obj.hash_value)            
    except:
        return redirect(url_for('log_in'))

    # hash_comparison is true if the password is correct. Log the user in.
    if hash_comparison == True:
        login_session['user_id'] = user_obj.id
        return redirect(url_for('posts'))
    else:
        return redirect(url_for('log_in'))


@app.route("/posts", methods=["GET", "POST"])
def posts():
    """ GET and POST for blog posts.
    
    GET request renders the posts template and passess the blog posts to the 
    template

    POST request inserts the new blog post into the database.
    """
    if request.method == "GET":
        try:
            user_id = login_session['user_id']
            posts = db.session.query(blog_post, app_user).filter(app_user.id == blog_post.poster_id).all()
            return render_template("posts.html", posts=posts)
        except:
            return "Sorry there has been an error."

    # POST 
    # Gather blog post data from the request 
    user_id = login_session['user_id']
    to_post = request.form["blogPost"]

    # insert the new post
    date_string = datetime.now().strftime("%m/%d/%Y %H:%M")
    insert_new_post(user_id, to_post, date_string)
    return "Thank you for posting."


app.debug = True
app.run(host='0.0.0.0', port=5000)
