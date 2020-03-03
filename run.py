import os
from config import Config
from backend import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.FLASK_PORT)
