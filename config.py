import os


class ConfigBase(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = "super-secret-key"


class Development(ConfigBase):
    DATABASE_URI = f"postgresql+psycopg2://admin:pass@localhost:5432/smartninja-forum"


class Production(ConfigBase):

    DATABASE_URI = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:5432/smartninja-forum"
