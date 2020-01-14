from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from backend.members.routes import member_api

    app.register_blueprint(member_api)

    return app
