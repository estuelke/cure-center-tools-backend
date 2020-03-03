import os
from config import Config
from backend import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=Config.FLASK_PORT)
