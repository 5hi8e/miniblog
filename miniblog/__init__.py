from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('miniblog.config')

    from miniblog.views.views import view
    app.register_blueprint(view)

    from miniblog.views.entries import entry
    app.register_blueprint(entry, url_prefix='/users')

    return app
