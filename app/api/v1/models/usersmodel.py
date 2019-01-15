import datetime

all_Users = []


class Users():
    """Class for all users functionality"""

    def signup(self, first_name, last_name, email, isAdmin):
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "isAdmin": isAdmin
            }

            all_Users.append(user)
            return user
