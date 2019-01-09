all_meetups = []


class Meetups():
    '''Initialize class variables the meetups model needs once it starts'''

    def __init__(self, meetup_id, createdOn, location, topic, happeningOn):
        self.meetup_id = len(all_meetups) + 1
        self.createdOn = createdOn
        self.location = location
        self.topic = topic
        self.happeningOn = happeningOn

    def create_meetup(self):
        pass
