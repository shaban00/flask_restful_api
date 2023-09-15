__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from app import ma


class CollegeSerializer(ma.Schema):
    class Meta:
        fields = (
            "ref_id",
            "college_name",
        )
