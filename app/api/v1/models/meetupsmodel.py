import datetime
all_meetups = []
all_rsvps = []


class Meetups():
    '''Initialize class variables the meetups model needs once it starts'''

    def create_meetup(self, id, location, topic, happeningOn, Tags):
        meetup = {"id": id,
                  "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
                  "location": location,
                  "topic": topic,
                  "happeningOn": happeningOn,
                  "Tags": Tags
                  }
        all_meetups.append(meetup)
        return meetup

    def get_all_meetups(self):
        return all_meetups

    def get_one_meetup(self, id):
        '''Get one meetup'''
        meetup_available = [
            meetup for meetup in all_meetups if meetup['id'] == id]
        return meetup_available

    # def create_rsvp(self, rsvp_id, response):
    #     rsvp_details = {
    #         "rsvp_id": rsvp_id,
    #         "meetup": meetup,
    #         "response": response}

    #     all_rsvps.append(rsvp_details)

    #     return rsvp_details
