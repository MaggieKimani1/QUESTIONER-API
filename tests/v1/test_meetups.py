import unittest
import json
from app import create_app
from app.api.v1.models.meetupsmodel import all_meetups, all_rsvps


class MeetupsTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.data = {
            "id": 1,
            "location": "kenya",
            "topic": "Tech",
            "happeningOn": "2/3/2018",
            "tags": "immigration"
        }

    def test_create_meetup(self):
        '''Test if admin can create a meetup'''
        response = self.client().post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        expected = "Meetup posted sucessfully"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get('message'), expected)

    def test_get_all_meetups(self):
        '''Test if user can get all meetup records'''
        self.client().post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        response = self.client().get('api/v1/meetups/upcoming',
                                     content_type="application/json")
        expected = "These are the available meetups"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("message"), expected)

    def test_unavailable_meetups(self):
        '''Test if user can get all meetup records'''
        response = self.client().get(
            'api/v1/meetups/upcoming', content_type="application/json")
        expected = "No meetup found"
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json.get("message"), expected)

    def test_get_one_meetup(self):
        '''Test if the user can get a specific meetup record'''
        self.client().post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        response = self.client().get(
            'api/v1/meetups/1', content_type="application/json")
        expected = "meetup retrieved"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get("message"), expected)

    def test_rsvp(self):
        '''Tests if a user can be able to rsvp to a specific meetup'''
        data = {
            "response": "yes"
        }
        self.client().post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        response = self.client().post(
            'api/v1/meetups/1/rsvps', data=json.dumps(data), content_type="application/json")
        expected = "RSVP saved for this meetup"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("message"), expected)

    def tearDown(self):
        all_meetups.clear()
        all_rsvps.clear()
