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
        try:
            id = int(id)
        except:
            return{"message": "The id has to be an integer"}, 400
        meetup_available = meetup.get_one_meetup(id)

        if not meetup_available:
            return {"message": "You cannot post a question to an unavailable meetup", "status": 400}, 400

        data = request.get_json()
        if not data:
            return{"message": "Question body cannot be empty", "status": 400}, 400

        meetup = id
        topic = data["topic"]
        body = data["body"]
        upvotes = data["upvotes"]
        downvotes = data["downvotes"]

        if not isinstance(id, int):
            return {"message": "Meetup must be an integer", "status": 400}, 400
        if not topic or topic.isspace():
            return {"message": "topic cannot be blank", "status": 400}, 400
        if not body or body.isspace():
            return {"message": "body must be provided", "status": 400}, 400

        new_question = Questions().create_question(
            meetup, topic, body, upvotes, downvotes)

        return {"data": new_question, "status": 400, "message": "Question posted successfully"}, 201


class SingleQuestion(Resource):
    '''Single question'''

    def patch(self, question_id):
        """Upvote or downvote a question"""
        try:
            question_id = int(question_id)
        except:
            return{"message": "The id has to be an integer"}, 400

        data = request.get_json()

        vote = data['vote']
        if vote != '+' and vote != '-':
            return "Vote can only be '+' or '-'"

        new_vote = Questions().upvote(question_id, vote)

        return {"status": 200, "data": new_vote, "message": "You have successfully voted"}, 200
