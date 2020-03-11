from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_mongoengine import MongoEngine
from config import Config


db = MongoEngine()


def create_app(config_class=Config):
    # Flask init
    app = Flask(__name__)
    app.config.from_object(config_class)

    # CORS init for frontend
    CORS(app, resources={r'*': {'origins': Config.FRONTEND}})

    # Database init
    db.init_app(app)

    # GraphQL init
    from backend.schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    return app
