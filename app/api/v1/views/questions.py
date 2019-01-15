from flask import Flask, request, jsonify, json
from flask_restful import Resource
from app.api.v1.models.questionsmodel import all_Questions, Questions
from app.api.v1.models.meetupsmodel import Meetups
from flask_expects_json import expects_json
from app.api.v1.utils.json_schema import question_schema


class AllQuestionsApi(Resource):
    '''Endpoint for all questions functionality'''
    @expects_json(question_schema)
    def post(self, id):
        """Endpoint for posting a question for a specific meetup"""
        meetup = Meetups()

        meetup_available = meetup.get_one_meetup(id)
        if not meetup_available:
            return {"message": "You cannot post a question to an unavailable meetup"}, 400

        data = request.get_json()
        if not data:
            return{"message": "Question body cannot be empty"}, 400

        meetup = id
        topic = data["topic"]
        body = data["body"]
        upvotes = data["upvotes"]
        downvotes = data["downvotes"]

        if not isinstance(data["meetup"], int):
            return {"message": "Meetup must be an integer"}, 400
        if not topic or topic.isspace():
            return {"message": "topic cannot be blank"}, 400

        new_question = Questions().create_question(
            meetup, topic, body, upvotes, downvotes)

        return {"data": new_question}, 201


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
