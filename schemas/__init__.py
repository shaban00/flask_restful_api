__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

DRAFT_4_SCHEMA = "http://json-schema.org/draft-04/schema#"
NULL_SCHEMA = {
    "type": "null"
}
STRING_SCHEMA = {
    "type": "string"
}
STRING_ARRAY_SCHEMA = {
    "type": "array", 
    "items": {
        "type": "string"
    }
}
INTEGER_SCHEMA = {
    "type": "integer"
}
BOOLEAN_SCHEMA = {
    "type": "boolean"
}
FLOAT_SCHEMA = {
    "type": "number"
}
NULLABLE_STRING_SCHEMA = {
    "anyOf": [STRING_SCHEMA, NULL_SCHEMA]
}
NULLABLE_INTEGER_SCHEMA = {
    "anyOf": [INTEGER_SCHEMA, NULL_SCHEMA]
}
EMAIL_SCHEMA = {
    "type": "string",
    "pattern": r"^[a-zA-Z0-9.\-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$"
}
NULLABLE_EMAIL_SCHEMA = {
    "anyOf": [EMAIL_SCHEMA, NULL_SCHEMA]
}



from .college import ADD_COLLEGE_SCHEMA
from .department import ADD_DEPARTMENT_SCHEMA
from .student import ADD_STUDENT_SCHEMA


SCHEMAS = {
    "add_college": ADD_COLLEGE_SCHEMA,
    "add_department": ADD_DEPARTMENT_SCHEMA,
    "add_student": ADD_STUDENT_SCHEMA
}
