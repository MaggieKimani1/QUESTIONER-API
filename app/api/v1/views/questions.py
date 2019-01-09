from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.questionsmodel import all_Questions, Questions


class AllQuestionsApi(Resource):
    '''Endpoint for all questions functionality'''

    def post(self):
        data = request.get_json()
        question_id = len(all_Questions)+1
        createdOn = data["createdOn"]
        createdBy = data["createdBy"]
        meetup = data["meetup"]
        topic = data["topic"]
        status = data["status"]

        new_question = Questions(
            question_id, createdOn, createdBy, meetup, topic, status).create_question()

        response = jsonify({"status": 201,
                            "data": new_question})
        response.status_code = 201
        return response
