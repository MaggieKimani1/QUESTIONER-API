from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.questionsmodel import all_Questions, Questions


class AllQuestionsApi(Resource):
    '''Endpoint for all questions functionality'''

    def post(self):
        """Endpoint for posting a question for a specific meetup"""
        data = request.get_json()

        createdBy = data["createdBy"]
        meetup = data["meetup"]
        topic = data["topic"]
        upvotes = 0
        downvotes = 0
        body = data["body"]

        new_question = Questions().create_question(createdBy,
                                                   meetup, topic, upvotes, downvotes, body)

        response = jsonify({"status": 201,
                            "data": new_question})
        response.status_code = 201
        return response


class SingleQuestion(Resource):
    '''Single question'''

    def patch(self, question_id):
        """Upvote or downvote a question"""

        data = request.get_json()

        vote = data['vote']
        print(vote)
        if vote != '+' and vote != '-':
            return "Vote can only be '+' or '-'"

        return Questions().upvote(question_id, vote)
