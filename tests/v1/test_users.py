import unittest
import json
from app import create_app
import datetime


class UsersTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = create_app('testing').test_client()
        self.data = {
            "first_name": "Maggie",
            "last_name": "Kimani",
            "email": "Maggiekim42@gmail.com",
            "isAdmin": "True",
        }

    def test_signup(self):
        '''Test if admin can create an account'''
        response = self.client.post(
            'api/v1/auth', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
