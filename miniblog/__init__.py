from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('miniblog.config')

db = SQLAlchemy(app)

from miniblog.views import views, entries
