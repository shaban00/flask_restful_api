__author__ = 'Shaban Hassan [shaban00]'

import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    MAIL_SERVER = ""
    MAIL_PORT = ""
    MAIL_USE_SSL = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""



class Development(Config):
    ENV = "development"
    DEBUG = True
    JSON_SORT_KEYS = False


class Production(Config):
    ENV = "production"
    DEBUG = False