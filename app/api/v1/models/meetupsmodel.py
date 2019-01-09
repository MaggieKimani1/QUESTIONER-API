all_meetups = []


class Meetups():
    '''Initialize class variables the meetups model needs once it starts'''

    def __init__(self, meetup_id, createdOn, location, topic, happeningOn, tags):
        self.meetup_id = len(all_meetups) + 1
        self.createdOn = createdOn
        self.location = location
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags

    def create_meetup(self):
        meetup = {"meetup_id": self.meetup_id,
                  "createdOn": self.createdOn,
                  "location": self.location,
                  "topic": self.topic,
                  "happeningOn": self.happeningOn,
                  "tags": self.tags
                  }
        all_meetups.append(meetup)
        return meetup

    def get_all_meetups(self):
        return all_meetups

    def get_one_meetup(self, meetup_id):
        for meetup in all_meetups:
            if meetup["meetup_id"] == meetup_id:
                return meetup
        return {"message": "Meetup not found"}, 404
