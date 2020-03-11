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
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DB'),
        'host': os.environ.get('MONGODB_HOST'),
        'port': int(os.environ.get('MONGODB_PORT')),
        'username': os.environ.get('MONGODB_USERNAME'),
        'password': os.environ.get('MONGODB_PASSWORD')
    }
    MONGODB_ADMIN_PASSWORD = os.environ.get('MONGODB_ADMIN_PASSWORD')

    # Helpers
    MEMBER_SEED_FILE = os.environ.get('MEMBER_SEED_FILE')
    COMPOUND_SEED_FILE = os.environ.get('COMPOUND_SEED_FILE')
