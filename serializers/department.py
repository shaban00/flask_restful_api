__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from app import ma
from .college import CollegeSerializer


class DepartmentSerializer(ma.Schema):
    class Meta:
        fields = (
            "ref_id",
            "department_name",
            "college",
        )

    college = ma.Nested(CollegeSerializer)
