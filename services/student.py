__author__ = 'Shaban Hassan [shaban00]'


from app import db
from models.student import Student
from models.department import Department
from utils import generate_uuid, get_current_time
from utils.exceptions import IntegrityError
from serializers.student import StudentSerializer


class StudentService:
    def add_student(self, fields: str):
        ref_id = generate_uuid()

        student = Student(ref_id=ref_id, **fields, created_at=get_current_time(), updated_at=get_current_time())
        db.session.add(student)

        try:
            db.session.commit()
        except Exception as e:
            error_orig = str(e.orig).replace("(", "").replace(")", "").split(",")[1].strip().replace("'", "").replace('"', '')
            raise IntegrityError(message=error_orig)

        return student

    def get_student(self, student_id: str):
        query = db.session.query(Student).filter_by(student_id=student_id).first()

        student_serializer = StudentSerializer()
        student = student_serializer.dump(query)

        return student

    def get_students(self, student_id: str = None):

        if student_id:
            student = self.get_student(student_id)
            return student

        else:
            query = db.session.query(Student).all()
            students_serializer = StudentSerializer(many=True)
            students = students_serializer.dump(query)

            return students

    def update_student(self):
        return None

    def remove_student(self):
        return None