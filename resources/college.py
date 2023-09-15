__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from flask import make_response, jsonify, request
from flask_restful import Resource
from services.college import CollegeService
from utils.validators import expect
from utils.exceptions import InvalidArgumentError


class CollegeResource(Resource):
    service = CollegeService()

    @expect("add_college", nested_in_data=True)
    def post(self):
        data = request.get_json()["data"]
        response = self.service.add_college(data)

        return make_response(
            jsonify({
                "result": f"{response} created successfully"
            }), 201
        )

    
    def get(self):
    
        keys = [key for key in request.args.keys()]

        ref_id = request.args.get("id")

        # if ref_id is None:
        #     raise InvalidArgumentError(message=f"Invalid argument {','.join(keys)}")


        response = self.service.get_colleges(ref_id)

        return make_response(
            jsonify({
                "data": response
            }), 200
        )
