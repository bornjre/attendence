import dashboard
import database
import admin

class App(object):
    def __init__(self):
        database.initDb()
        adminpanel = admin.Admin()
        verified = adminpanel.start()
        if verified:

            self.dashboard = dashboard.Dashboard()
        print("I DO NOT LIKE UNVERIFIED PEOPLE")


if __name__ == "__main__":
    app = App()
