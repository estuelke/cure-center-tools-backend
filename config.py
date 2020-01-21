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
