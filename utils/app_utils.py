import os

import config


def get_config():
    env = os.getenv("FLASK_ENV", "production")
