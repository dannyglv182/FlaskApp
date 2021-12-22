from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import psql_login
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = psql_login
db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

# app.debug = True
# app.run(host='0.0.0.0', port=5000)
