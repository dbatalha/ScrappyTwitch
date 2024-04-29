import configparser


class PropertiesReader:
    # Defining constants
    TWITCH_CONTEXT = "Twitch"
    PERSISTENCE = "Persistence"
    LOGS = "Logs"
    CONFIG_FILE = "scrappy_bot/resources/config.ini"

    client_id = None
    client_secret = None
    grant_type = None

    persistence_url = None

    file_location = None
    scrappy_bot = None

    config = None

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)
        self.__twitch_properties()
        self.__persistence_properties()
        self.__logging_properties()

    def __logging_properties(self):
        self.set_file_location(self.config.get(self.LOGS, "file_location"))
        self.set_scrappy_bot(self.config.get(self.LOGS, "scrappy_bot"))

    def __twitch_properties(self):
        self.set_client_id(self.config.get(self.TWITCH_CONTEXT, "client_id"))
        self.set_client_secret(self.config.get(self.TWITCH_CONTEXT, "client_secret"))
        self.set_grant_type(self.config.get(self.TWITCH_CONTEXT, "grant_type"))

    def __persistence_properties(self):
        self.set_persistence_url(self.config.get(self.PERSISTENCE, "persistence_ms_url"))

    def set_persistence_url(self, url):
        self.persistence_url = url

    def get_persistence_url(self):
        return self.persistence_url

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_client_secret(self):
        return self.client_secret

    def set_client_secret(self, client_secret):
        self.client_secret = client_secret

    def get_grant_type(self):
        return self.grant_type

    def set_grant_type(self, grant_type):
        self.grant_type = grant_type

    def set_file_location(self, file_location):
        self.file_location = file_location

    def set_scrappy_bot(self, scrappy_bot):
        self.scrappy_bot = scrappy_bot

    def get_file_location(self):
        return self.file_location

    def get_scrappy_bot(self):
        return self.scrappy_bot
