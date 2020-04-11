__author__ = "Shaban Hassan [shaban00]"

from app import ma


class CollegeSerializer(ma.Schema):
    class Meta:
        fields = (
            "ref_id",
            "college_name",
        )
