all_Questions = []


class Questions():
    '''Initialize class variables the questions model needs once it starts'''

    def __init__(self, question_id, createdOn, createdBy, meetup, topic, status):
        self.question_id = len(all_Questions)+1
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.meetup = meetup
        self.topic = topic
        self.status = status

    def create_question(self):
        question_payload = {
            "question_id": self.question_id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "meetup": self.meetup,
            "topic": self.topic,
            "status": self.status
        }
        all_Questions.append(question_payload)
        return question_payload
