from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('miniblog.config')
    if test_config:
        app.config.from_mapping(test_config)

    db.init_app(app)

    from miniblog.views.views import view
    app.register_blueprint(view)

    from miniblog.views.entries import entry
    app.register_blueprint(entry, url_prefix='/users')

    return app
