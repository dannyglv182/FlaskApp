from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

# app.debug = True
# app.run(host='0.0.0.0', port=5000)
