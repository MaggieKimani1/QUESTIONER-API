from flask import Flask, request, jsonify, make_response
from flask_restful import Resource
from app.api.v1.models.meetupsmodel import all_meetups, Meetups, all_rsvps


class AllMeetupsApi(Resource):
    """Endpoint for all meetups functionality"""

    def post(self):
        """This endpoint creates a meetup record"""
        data = request.get_json()

        if not data:
            return "Please provide the required details", 400

        id = len(all_meetups) + 1
        location = data["location"]
        topic = data["topic"]
        happeningOn = data["happeningOn"]
        tags = data["tags"]

        if not location or location.isspace():
            return make_response(jsonify({"message": "location must be provided"}), 400)
        if not topic or topic.isspace():
            return make_response(jsonify({"message": "topic must be provided"}), 400)
        if not happeningOn or happeningOn.isspace():
            return make_response(jsonify({"message": "happeningOn must be provided"}), 400)
        if not tags:
            return make_response(jsonify({"message": "tags must be provided"}), 400)
        meetup_record = Meetups().create_meetup(id, location, topic, happeningOn, tags)
        response = jsonify({"status": 201, "data": meetup_record})
        response.status_code = 201
        return response

    def get(self):
        """Endpoint for geting all meetup records"""

        meetups = Meetups().get_all_meetups()
        if meetups:
            response = jsonify({"status": 200,
                                "data": meetups})
            response.status_code = 200
            return response
        return {"message": "No meetup found"}, 404


class SingleMeetupApi(Resource):
    '''Endpoint for single meetup functionality'''

    def get(self, id):
        '''Fetching a single meetup'''
        meetup_available = Meetups().get_one_meetup(id)

        if meetup_available:
            return {'Meetup': meetup_available,
                    }, 200
        return {"message": "That meetup_id does not exist"}, 404

    def post(self, id):
        '''Post an RSVP'''
        data = request.get_json()
        if not data:
            "Please submit your RSVP", 400
        response = data['response']

        if (response != "yes" and response != "no" and response != "maybe"):
            return {"error": "response should be a yes, no or maybe"}

        meetup_available = Meetups().get_one_meetup(id)
        if not meetup_available:
            return "You cannot RSVP an unavailable meetup", 400
        return {"status": 201,
                "data": [{
                    "meetup": id,
                    "response": response
                }]}
