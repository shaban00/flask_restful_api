__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from app import db
from models.college import College
from utils import generate_uuid, get_current_time
from utils.exceptions import IntegrityError
from serializers.college import CollegeSerializer


class CollegeService:
    def add_college(self, fields: dict):
        ref_id = generate_uuid()

        college = College(ref_id=ref_id, **fields, created_at=get_current_time(), updated_at=get_current_time())
        db.session.add(college)

        try:
            db.session.commit()
        except Exception as e:
            error_orig = str(e.orig).replace("(", "").replace(")", "").split(",")[1].strip().replace("'", "").replace('"', '')
            raise IntegrityError(message=error_orig)
        
        return college


    def get_college(self, ref_id: str):
        query = db.session.query(College).filter_by(ref_id=ref_id).first()
        college_serializer = CollegeSerializer()
        college = college_serializer.dump(query)

        return college


    def get_colleges(self, ref_id: str = None):

        if ref_id:
            college = self.get_college(ref_id)
            return college
            
        else:
            query = db.session.query(College).all()
            college_serializer = CollegeSerializer(many=True)
            colleges = college_serializer.dump(query)

            return colleges


    def update_college(self):
        return None


    def remove_college(self):
        return None
