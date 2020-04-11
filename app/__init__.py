__author__ = 'Shaban Hassan [shaban00]'

from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils import load_config
from dotenv import load_dotenv
load_dotenv()


""" Database connection """
db = SQLAlchemy()

""" Marshmallow serialization """
ma = Marshmallow()


""" SocketIO connection """
socketio = SocketIO(logger=False, engineio_logger=False)

""" Function to create Flask app """

def create_app():
    """ 
        Create flask app

        Returns:
            Flask -> Flask app
     """
     
    app: Flask = Flask(__name__)

    """ Load Flask configurations """
    app.config.from_object(load_config())

    """ Initialize database """
    db.init_app(app)

    """ Initialize marshmallow """
    ma.init_app(app)
    mail = Mail(app)
    CORS(app)

    return app, mail