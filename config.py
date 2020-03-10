import os
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    # Used for CORS configuration
    FRONTEND = os.environ.get('FRONTEND')

    # Environment-based
    FLASK_PORT = os.environ.get('FLASK_PORT', default=5000)
    HOST = os.environ.get('HOST', default='127.0.0.1')
    LOCAL = os.environ.get('LOCAL', default=False)

    # SQLite3 Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, os.environ.get('SQLALCHEMY_DATABASE_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mongo DB
    MONGO_USER = os.environ.get('MONGO_USER')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
    MONGO_DATABASE_NAME = os.environ.get('MONGO_DATABASE_NAME')
    MONGO_DATABASE_ROUTE = os.environ.get('MONGO_DATABASE_ROUTE')
    MONGO_DATABASE_PORT = os.environ.get('MONGO_DATABASE_PORT')

    # Helpers
    MEMBER_SEED_FILE = os.environ.get('MEMBER_SEED_FILE')
    COMPOUND_SEED_FILE = os.environ.get('COMPOUND_SEED_FILE')