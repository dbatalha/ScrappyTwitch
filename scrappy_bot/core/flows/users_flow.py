from scrappy_bot.core.presistance.mongodb_client import MongoDBClient
from scrappy_bot.core.properties_reader import PropertiesReader


class UsersFlow:
    USERS = "Users"
    DATABASE = "Scrappy"

    mongodb_client = None

    def __init__(self):
        properties = PropertiesReader()
        self.mongodb_client = MongoDBClient(properties.get_connection_string())

    def _users_setup(self):
        self.mongodb_client.set_database(self.DATABASE)
        self.mongodb_client.set_collection(self.USERS)

    def save_user(self, user):
        self._users_setup()

        found_document = self.mongodb_client.find_one_element("_id", user.get_user_id())
        if found_document:
            pass
        else:
            self.mongodb_client.insert_one_collection(user)

        self.mongodb_client.close()
