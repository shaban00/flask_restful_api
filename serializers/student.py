__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from app import ma
from .department import DepartmentSerializer


class StudentSerializer(ma.Schema):
    class Meta:
        fields = (
            "ref_id",
            "student_id",
            "first_name",
            "last_name",
            "username",
            "email",
            "department",
        )

    department = ma.Nested(DepartmentSerializer)
