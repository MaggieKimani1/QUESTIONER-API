from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.usersmodel import all_Users, Users


class AllUsersApi(Resource):
    '''Endpoint for all users functionality'''

    def post(self):
        data = request.get_json()

        if not data:
            return "Data must be in JSON format", 404
        try:
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            isAdmin = data["isAdmin"]

            User = Users().signup(first_name, last_name, email, isAdmin)
            if User:
                response = jsonify({"status": 201,
                                    "data": User})
                response.status_code = 201

                return response
            else:
                return 'Could not create an account', 400

        except:
            return "Please include all details", 400
