__author__ = 'Shaban Hassan [shaban00]'

from flask import g
import os
from .config import Config, Development, Production
from .auth_user import AuthUser
import logging
from utils.exceptions import AuthenticationError
import jwt
from typing import List
import uuid
import datetime


def is_in_development():
    return False if os.environ.get("MODE") == "PRODUCTION" else True


def load_config():
    return Development if is_in_development() else Production


def jwt_encode_payload(payload):
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithms=['HS256'])


def decode_jwt(token: str):
    return jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])


def set_current_user(ref_id:str, privileges: List = [], **kwargs):
    user_data = {
        "ref_id": ref_id,
        "privileges": privileges or []
    }
    user_data.update(kwargs)
    setattr(g, "user", user_data)


def get_current_user():
    try:
        user_data = getattr(g, "user")
    except Exception as error:
        logging.error(error)
        raise AuthenticationError()
    return AuthUser(**user_data)


def generate_uuid():
    id = uuid.uuid4()
    return str(id)
    

def get_current_time():
    return datetime.datetime.utcnow()
