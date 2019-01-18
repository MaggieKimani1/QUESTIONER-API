import unittest
import json
from app import create_app
from app.api.v1.models.questionsmodel import all_Questions


class QuestionsTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        self.data = {
            "meetup": 1,
            "topic": "Tech",
            "body": "What is python?",
            "upvotes": 4,
            "downvotes": 6
        }
        self.data2 = {
            "id": 1,
            "location": "kenya",
            "topic": "Tech",
            "happeningOn": "2/3/2018",
            "tags": "immigration"
        }

    def test_create_question(self):
        '''Test if user can create a question'''
        self.client().post('api/v1/meetups', data=json.dumps(self.data2),
                           content_type="application/json")
        response = self.client().post('api/v1/meetups/1/questions',
                                      data=json.dumps(self.data), content_type="application/json")

        expected = "Question posted successfully"
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get('message'), expected)

    def test_vote(self):
        '''Test if user can either downvote or upvote a question'''
        self.client().post('api/v1/meetups', data=json.dumps(self.data),
                           content_type="application/json")
        self.client().post('api/v1/meetups/1/questions',
                           data=json.dumps(self.data), content_type="application/json")

        vote = {"vote": "-"}
        response = self.client().patch('api/v1/questions/1', data=json.dumps(vote),
                                       content_type="application/json")

        expected = "You have successfully voted"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('message'), expected)

    def tearDown(self):
        all_Questions.clear()
