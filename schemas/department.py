__author__ = 'Shaban Hassan [shaban00]'

from . import DRAFT_4_SCHEMA, STRING_SCHEMA

ADD_DEPARTMENT_SCHEMA = {
    "$schema": DRAFT_4_SCHEMA,
    "type": "object",
    "properties": {
        "department_name": STRING_SCHEMA,
        "college_ref_id": STRING_SCHEMA
    },
    "additionalProperties": False,
    "required": ["department_name", "college_ref_id"]
}