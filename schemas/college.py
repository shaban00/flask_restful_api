__author__ = 'Shaban Hassan [shaban00]'

from . import DRAFT_4_SCHEMA, STRING_SCHEMA

ADD_COLLEGE_SCHEMA = {
    "$schema": DRAFT_4_SCHEMA,
    "type": "object",
    "properties": {
        "college_name": STRING_SCHEMA
    },
    "additionalProperties": False,
    "required": ["college_name"]
}