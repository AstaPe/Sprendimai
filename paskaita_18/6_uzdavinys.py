class UserSession:
    def __init__(self):
        self.logged_in = False
        self.user_data = None

    def login(self, username, password):
        if self.authenticate(username, password):
            self.logged_in = True
            self.user_data = self.get_user_data(username)
            print("Logged in successfully.")
        else:
            print("Login failed. Incorrect username or password.")

    def logout(self):
        self.logged_in = False
        self.user_data = None
        print("Logged out successfully.")

    def is_logged_in(self):
        return self.logged_in

    def get_user_data(self):
        if self.is_logged_in():
            return self.user_data
        else:
            print("User is not logged in.")
            return None

    def authenticate(self, username, password):
        return username == "admin" and password == "admin"

    def get_user_data(self, username):
        return {"username": username, "email": "example@example.com"}


session = UserSession()
session.login("admin", "admin")
print("Is logged in:", session.is_logged_in())
print("User data:", session.get_user_data())
session.logout()
print("Is logged in:", session.is_logged_in())
print("User data:", session.get_user_data())