import datetime

all_Users = []


class Users():

    def signup(self, first_name, last_name, email, isAdmin):
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "isAdmin": isAdmin
        }

        all_Users.append(user)
        return user

    def user_login(self, email, password):
                        # logged_user = {
                        #     "email": email.
                        #     "password": password
                        # }
        logged_user = [user for user in all_Users if user["email"]
                       == email]

        if not logged_user:
            return "User does not exist", 400
        if logged_user["password"] == password:
            return "Successfully logged in", 201
