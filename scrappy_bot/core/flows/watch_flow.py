from scrappy_bot.core.presistance.mongodb_client import MongoDBClient
from scrappy_bot.core.properties_reader import PropertiesReader


class WatchFlow:
    WATCHERS = "Watchers"
    DATABASE = "Scrappy"

    mongodb_client = None

    def __init__(self):
        properties = PropertiesReader()
        self.mongodb_client = MongoDBClient(properties.get_connection_string())

    def _watch_setup(self):
        self.mongodb_client.set_database(self.DATABASE)
        self.mongodb_client.set_collection(self.WATCHERS)

    def add_watcher(self, watcher):
        self._watch_setup()

        found_document = self.mongodb_client.find_one_element("name", watcher.get_name())
        if found_document:
            pass
        else:
            self.mongodb_client.insert_one_collection(watcher)

    def get_all_watchers(self):
        self._watch_setup()

        return self.mongodb_client.find_all()
