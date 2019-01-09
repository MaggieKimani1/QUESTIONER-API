from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.meetupsmodel import all_meetups, Meetups


class AllMeetupsApi(Resource):
    '''Endpoint for all meetups functionality'''

    def post(self):
        data = request.get_json()
        meetup_id = len(all_meetups) + 1
        createdOn = data["createdOn"]
        location = data["location"]
        topic = data["topic"]
        tags = data["tags"]
        happeningOn = data["happeningOn"]

        meetup_record = Meetups(meetup_id, createdOn, location, topic,
                                happeningOn, tags).create_meetup()

        response = jsonify({"status": 201,
                            "data": meetup_record})
        response.status_code = 201
        return response

    def get(self):
        '''Endpoint for getting all meetup records'''

        meetups = Meetups.get_all_meetups(self)
        response = jsonify({"status": 200,
                            "data": meetups})
        response.status_code = 200
        return response


class SingleMeetupApi(Resource):
    '''Endpoint for single meetup functionality'''

    def get(self, meetup_id):
        single_meetup = Meetups.get_one_meetup(self, meetup_id)
        response = jsonify({"status": 200,
                            "data": single_meetup})
        response.status_code = 200
        return response
