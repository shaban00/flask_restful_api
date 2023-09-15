__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from typing import Callable
import jsonschema
from flask import request
from functools import wraps
from schemas import DRAFT_4_SCHEMA, SCHEMAS
from utils.exceptions import JSONDataValidatorError


def expect(schema_name: str = "", nested_in_data: bool = True, is_multiple: bool = False) -> Callable:
    def wrapper_func(func):
        @wraps(func)
        def decorated(*args, **kwargs):

            try:
                payload = request.get_json()["data"] if nested_in_data else request.get_json()
            except KeyError as e:
                raise JSONDataValidatorError(message=str(e), payload={"path": f"expected {e}"})

            except TypeError:
                raise JSONDataValidatorError(message="Invalid json data", payload={"path": "expected key `data`"})


            try:
                if is_multiple:
                    schema = {
                        "$schema": DRAFT_4_SCHEMA,
                        "type": "array",
                        "items": SCHEMAS[schema_name]
                    }
                else:
                    schema = SCHEMAS[schema_name]
            
            except KeyError:
                raise Exception(f"Schema name {schema_name} is not registered")

            try:
                jsonschema.validate(payload, schema)
                return func(*args, **kwargs)
            
            except jsonschema.exceptions.ValidationError as error:   
                details = {
                    "path": "/%s%s%s" % (
                        "data" if nested_in_data else "",
                        "[]/" if is_multiple else "",
                        "/".join(
                            str(path) for path in list(error.absolute_path)[1::2])
                    )
                }
                raise JSONDataValidatorError(message=error.message, payload=details)
            
            except IndexError as error:
                details = {
                    "path": ""
                }
                raise JSONDataValidatorError(message=error.message, payload=details)
        return decorated
    return wrapper_func
