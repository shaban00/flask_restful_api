__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from flask import make_response, jsonify, request
from flask_restful import Resource
from services.department import DepartmentService
from utils.validators import expect
from utils.exceptions import InvalidArgumentError


class DepartmentResource(Resource):
    service = DepartmentService()

    @expect("add_department", nested_in_data=True)
    def post(self):
        data = request.get_json()["data"]
        response = self.service.add_department(data)

        return make_response(
            jsonify({
                "result": f"{response} created successfully"
            }), 201
        )


    def get(self):
        keys = [key for key in request.args.keys()]
        ref_id = request.args.get("id")

        # if not ref_id:
        #     raise InvalidArgumentError(message=f"Invalid argument {','.join(keys)}")

        response = self.service.get_departments(ref_id)

        return make_response(
            jsonify({
                "data": response
            }), 200
        )
