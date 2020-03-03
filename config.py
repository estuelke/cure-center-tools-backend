import os
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    FRONTEND = os.getenv('FRONTEND')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MEMBER_SEED_FILE = os.environ.get('MEMBER_SEED_FILE')
    COMPOUND_SEED_FILE = os.environ.get('COMPOUND_SEED_FILE')
    FLASK_PORT = os.environ.get('FLASK_PORT', default=5000)
    HOST = os.environ.get('HOST', default='127.0.0.1')