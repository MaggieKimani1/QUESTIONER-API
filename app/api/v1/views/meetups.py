from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.meetupsmodel import all_meetups, Meetups, all_rsvps
from flask_expects_json import expects_json
from app.api.v1.utils.json_schema import meetup_schema


class AllMeetupsApi(Resource):
    """Endpoint for all meetups functionality"""

    @expects_json(meetup_schema)
    def post(self):
        """This endpoint creates a meetup record"""
        data = request.get_json()

        if not data:
            return {"message": "Please provide the required details", "status": 400}, 400

        id = len(all_meetups) + 1
        location = data["location"]
        topic = data["topic"]
        happeningOn = data["happeningOn"]
        tags = data["tags"]

        if not location or location.isspace():
            return {"message": "location must be provided", "status": 400}, 400
        if not topic or topic.isspace():
            return {"message": "topic must be provided", "status": 400}, 400
        if not happeningOn or happeningOn.isspace():
            return {"message": "happeningOn must be provided", "status": 400}, 400
        if not tags:
            return {"message": "tags must be provided", "status": 400}, 400
        meetup_record = Meetups().create_meetup(id, location, topic, happeningOn, tags)

        return {"status": 201, "data": meetup_record}, 201

    def get(self):
        """Endpoint for geting all meetup records"""

        meetups = Meetups().get_all_meetups()
        if meetups:
            return {"status": 200, "data": meetups}, 200
        return {"message": "No meetup found", "status": 404}, 404


class SingleMeetupApi(Resource):
    '''Endpoint for single meetup functionality'''

    def get(self, id):
        '''Fetching a single meetup'''
        meetup_available = Meetups().get_one_meetup(id)

        if meetup_available:
            return {'Meetup': meetup_available,
                    }, 200
        return {"message": "That meetup_id does not exist", "status": 404}, 404

    def post(self, id):
        '''Post an RSVP'''
        meetup_available = Meetups().get_one_meetup(id)
        if not meetup_available:
            return {"message": "You cannot RSVP an unavailable meetup"}, 400
        data = request.get_json()
        if not data:
            {"message": "Please submit your RSVP", "status": 400}, 400
        response = data['response']

        if (response == "yes" or response == "no" or response == "maybe"):
            return {"status": 201,
                    "data": [{
                        "meetup": id,
                        "response": response
                    }]}, 201
        else:
            return {"message": "response should be a yes, no or maybe", "status": 400}, 400
