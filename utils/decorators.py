__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from functools import wraps
from logging import info
from logging import warn
from flask import g, request
from .exceptions import AuthenticationError, InvalidAuthorizationHeader
from . import decode_jwt


def authenicate_request(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not request.headers.get("Authorization"):
            raise AuthenticationError()

        user_data = dict()

        try:
            token = request.headers.get("Authorization").split()[1]

            if token:
                try:
                    user_data = decode_jwt(token)
                except:
                    raise InvalidAuthorizationHeader()
        except:
            raise AuthenticationError()

        setattr(g, "user_data", user_data)

        return func(*args, **kwargs)

    return decorated
