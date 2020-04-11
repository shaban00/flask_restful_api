__author__ = 'Shaban Hassan [shaban00]'

import datetime
from app import db


class Student(db.Model):

    """ Table name """
    __tablename__ = "students"

    """ Columns """

    ref_id = db.Column(db.String(255), primary_key=True)
    student_id = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    gender = db.Column(db.String(45))
    email = db.Column(db.String(255))
    password = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    department_ref_id = db.Column(db.String(255), db.ForeignKey("departments.ref_id"))

    """ Relationships """

    department = db.relationship("Department", foreign_keys=[department_ref_id])


    def __init__(self, ref_id, student_id, first_name, last_name, username, gender, email, password, created_at, updated_at, department_ref_id):
        self.ref_id = ref_id
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.department_ref_id = department_ref_id


    def __repr__(self):
        return f"{self.student_id}"