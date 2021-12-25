from models import db
from models import app_user, blog_post, p_word


def insert_new_password(hash_string):
    to_store = p_word(hash_value=hash_string)
    db.session.add(to_store)
    db.session.commit() 
    return to_store


def insert_new_user(user_name_string, password_id):
    to_store = app_user(user_name=user_name_string, password=password_id)
    db.session.add(to_store)
    db.session.commit()
    return to_store


