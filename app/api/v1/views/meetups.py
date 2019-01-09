from flask import Flask, request, make_response, jsonify
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
