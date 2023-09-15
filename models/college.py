__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

import datetime
from app import db


class College(db.Model):

    """ Table name """

    __tablename__ = "colleges"

    """ Table columns """

    ref_id = db.Column(db.String(255), primary_key=True)
    college_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)



    def __init__(self, ref_id, college_name, created_at, updated_at):
        self.ref_id = ref_id
        self.college_name = college_name
        self.created_at = created_at
        self.updated_at = updated_at


    def __repr__(self):
        return f"{self.college_name}"
