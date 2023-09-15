__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from . import DRAFT_4_SCHEMA, STRING_SCHEMA, INTEGER_SCHEMA, EMAIL_SCHEMA

ADD_STUDENT_SCHEMA = {
    "$schema": DRAFT_4_SCHEMA,
    "type": "object",
    "properties": {
        "student_id": STRING_SCHEMA,
        "first_name": STRING_SCHEMA,
        "last_name": STRING_SCHEMA,
        "username": STRING_SCHEMA,
        "gender": STRING_SCHEMA,
        "email": EMAIL_SCHEMA,
        "password": STRING_SCHEMA,
        "department_ref_id": STRING_SCHEMA
    },
    "additionalProperties": False,
    "required": ["student_id", "first_name", "last_name", "username", "gender", "email", "password", "department_ref_id"]
}
