from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('miniblog.config')

db = SQLAlchemy(app)

from miniblog.views.views import view
app.register_blueprint(view)

from miniblog.views.entries import entry
app.register_blueprint(entry, url_prefix='/users')
