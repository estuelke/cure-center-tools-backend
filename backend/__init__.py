from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    if Config.LOCAL:
        CORS(app, resources={r'*': {'origins': Config.FRONTEND}})

    db.init_app(app)
    migrate.init_app(app, db)

    # Routes/Blueprints
    from backend.members.routes import member_api
    # from backend.compound.routes import compound_api

    app.register_blueprint(member_api)
    # app.register_blueprint(compound_api)

    return app
