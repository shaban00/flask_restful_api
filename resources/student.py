__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from flask import make_response, jsonify, request
from flask_restful import Resource
from services.student import StudentService
from utils.validators import expect
from utils.exceptions import InvalidArgumentError
from utils.decorators import authenicate_request


class StudentResource(Resource):
    service = StudentService()

    @expect("add_student", nested_in_data=True)
    def post(self):
        data = request.get_json()["data"]
        response = self.service.add_student(data)

        return make_response(
            jsonify({"result": f"{response} created successfully"}), 201
        )

    def get(self):
        keys = [key for key in request.args.keys()]
        student_id = request.args.get("student_id")

        response = self.service.get_students(student_id)

        return make_response(jsonify({"data": response}), 200)

