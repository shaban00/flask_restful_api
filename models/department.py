__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

import datetime
from app import db



class Department(db.Model):

    """ Table name """
    __tablename__ = "departments"

    """ Table columns """
    ref_id = db.Column(db.String(255), primary_key=True)
    department_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    college_ref_id = db.Column(db.String(255), db.ForeignKey("colleges.ref_id"))


    """ Relationships """

    # department_college = db.relationship("College", foreign_keys=[college_ref_id])
    college = db.relationship("College", foreign_keys=[college_ref_id])


    def __init__(self, ref_id, department_name, college_ref_id, created_at, updated_at):
        self.ref_id = ref_id
        self.department_name = department_name
        self.college_ref_id = college_ref_id
        self.created_at = created_at
        self.updated_at = updated_at


    def __repr__(self):
        return f"{self.department_name}"
