__author__ = 'Shaban Hassan [shaban00]'


from app import db
from models.department import Department
from models.college import College
from utils import generate_uuid, get_current_time
from utils.exceptions import IntegrityError
from serializers.department import DepartmentSerializer


class DepartmentService:
    def add_department(self, fields: str):
        ref_id = generate_uuid()

        department = Department(ref_id=ref_id, **fields, created_at=get_current_time(), updated_at=get_current_time())
        db.session.add(department)

        try:
            db.session.commit()
        except Exception as e:
            print(str(e.orig))
            error_orig = str(e.orig).replace("(", "").replace(")", "").split(",")[1].strip().replace("'", "").replace('"', '').split(":")[0]
            raise IntegrityError(message=error_orig)

        return department

    def get_department(self, ref_id: str):
        query = db.session.query(Department).filter_by(ref_id=ref_id).first()

        department_serializer = DepartmentSerializer()
        department = department_serializer.dump(query)

        return department

    def get_departments(self, ref_id: str = None):

        if ref_id:
            department = self.get_department(ref_id)
            return department
            
        else:
            query = db.session.query(Department).all()
            department_serializer = DepartmentSerializer(many=True)

            departments = department_serializer.dump(query)

            return departments

    def update_department(self):
        return None

    def remove_department(self):
        return None