import datetime

all_Users = []


class Users():

    def __init__(self):
        pass

        def signup(self, firstname, lastname, email, registered, isAdmin):
            user = {
                "firstname": "Maggie",
                "lastname": "Kimani",
                "email": "maggiekim42@gmail.com",
                "registered": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
                "isAdmin": "True"
            }

            all_Users.append(user)
