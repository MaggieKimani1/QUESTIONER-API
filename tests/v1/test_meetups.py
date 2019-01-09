import unittest
import json
from app import create_app
import os


class MeetupsTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = create_app('testing').test_client()
        self.data = {
            "meetup_id": 1,
            "createdOn": "Date",
            "location": "String",
            "topic": "String",
            "happeningOn": "Date",
        }

    def test_create_meetup(self):
        '''Test if admin can create a meetup'''
        response = self.client.post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)


'''Standard unittest runner for executing the test'''
if __name__ == '__main__':
    unittest.main()
