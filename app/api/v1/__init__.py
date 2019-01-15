from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups import AllMeetupsApi, SingleMeetupApi
from app.api.v1.views.questions import AllQuestionsApi, SingleQuestion
from app.api.v1.views.users import AllUsersApi


# create variable called api_v1 that defines the blueprint and registers it in the application factory
app_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(app_v1)

api_v1.add_resource(AllMeetupsApi, '/meetups', '/meetups/upcoming')
api_v1.add_resource(
    SingleMeetupApi, '/meetups/<int:id>', '/meetups/<int:id>/rsvps')
# api_v1.add_resource(RsvpApi, '/meetups/<int:id>/rsvps/<int:rsvp_id>')
api_v1.add_resource(AllQuestionsApi, '/questions')
api_v1.add_resource(SingleQuestion, '/questions/<int:question_id>')
api_v1.add_resource(AllUsersApi, '/auth')
