import unittest
import json
from app import create_app
import datetime


class UsersTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = create_app('testing').test_client()
        self.data = {"id": 1,
                     "firstname”: "Maggie",
                     "lastname": "Kimani",
                     "email": "Maggiekim42@gmail.com",
                     "registered": ""
                     "isAdmin": True,
                     }

    def test_create_user_account(self):
        '''Test if admin can create a meetup'''
        response = self.client.post(
            'api/v1/users', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
