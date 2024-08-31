from models import db
from models import app_user, blog_post, p_word
from flask_sqlalchemy import SQLAlchemy


def insert_new_password(hash_string):
    """ Inserts a new hash value into the database."""
    to_store = p_word(hash_value=hash_string)
    db.session.add(to_store)
    db.session.commit() 
    return to_store


def insert_new_user(user_name_string, password_id):
    """ Inserts a user into the database."""
    to_store = app_user(user_name=user_name_string, password=password_id)
    db.session.add(to_store)
    db.session.commit()
    return to_store


def username_exists(user_name_string):
    """ Returns True if a username already exists.
    """
    try:
        exists = db.session.query(app_user).filter_by(user_name=user_name_string).one()
        print (exists)
        return True
    except:
        return False


def insert_new_post(poster_id, text, date_string):
    """ Inserts a new blog post """
    try:
        to_store = blog_post(poster_id=poster_id, text=text, date=date_string)
        db.session.add(to_store)
        db.session.commit()
        return True
    except:
        return False
