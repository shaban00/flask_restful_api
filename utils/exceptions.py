__author__ = 'Shaban Hassan [shaban00]'

from typing import Dict
from flask import make_response, jsonify


class BaseError(Exception):

    def __init__(self, message: str, error_code: int = 400, payload: [Dict, None] = None, *args) -> None:
        super(BaseError, self).__init__(*args)
        self.message = message
        self.error_code = error_code
        self.payload = payload


    def to_dict(self) -> Dict:
        response = {
            "message": self.message
        }

        if self.payload:
            response["data"] = self.payload

        return response



class JSONDataValidatorError(BaseError):

    def __init__(self, message: str, payload: [Dict, None], error_code: int = 422) -> None:
        super(JSONDataValidatorError, self).__init__(
            message=message, error_code=error_code, payload=payload
        )


class AuthenticationError(BaseError):

    def __init__(self):
        super(AuthenticationError, self).__init__(
            message="Authentication Failed", error_code=401
        )


class PrivilegesError(BaseError):

    def __init__(self):
        super(PrivilegesError, self).__init__(
            message="Privileges Error, Access Denied", error_code=401
        )


class InvalidAuthorizationHeader(BaseError):

    def __init__(self):
        super(InvalidAuthorizationHeader, self).__init__(
            message="Invalid Authorization Header", error_code=401
        )


class IntegrityError(BaseError):
    
    def __init__(self, message: str):
        super(IntegrityError, self).__init__(
            message=message, error_code=400
        )


class InvalidArgumentError(BaseError):

    def __init__(self, message: str):
        super(InvalidArgumentError, self).__init__(
            message=message, error_code=400
        )