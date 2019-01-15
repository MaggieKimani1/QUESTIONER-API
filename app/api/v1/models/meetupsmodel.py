import datetime
all_meetups = []
all_rsvps = []


class Meetups():
    '''Initialize class variables the meetups model needs once it starts'''

    def create_meetup(self, id, location, topic, happeningOn, tags):
        meetup = {"id": len(all_meetups)+1,
                  "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
                  "location": location,
                  "topic": topic,
                  "happeningOn": happeningOn,
                  "tags": tags
                  }
        all_meetups.append(meetup)
        return meetup

    def get_all_meetups(self):
        """method for getting all upcoming meetups"""
        return all_meetups

    def get_one_meetup(self, id):
        '''Get one meetup'''
        meetup_available = [
            meetup for meetup in all_meetups if meetup['id'] == id]
        return meetup_available
