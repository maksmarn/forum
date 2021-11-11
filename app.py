from sqla_wrapper import SQLAlchemy
from flask import Flask

import config


def create_app(env: str = "development") -> Flask:
    app = Flask(__name__)

    if env == "development":
        app.config.from_object(config.Development)
    elif env == "production":
        app.config.from_object(config.Production)

    app.secret_key = os.getenv("SECRET_KEY", secrets.token_hex(20))

    return app
