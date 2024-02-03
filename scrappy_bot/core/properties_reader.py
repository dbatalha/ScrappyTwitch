import configparser


class PropertiesReader:
    # Defining constants
    TWITCH_CONTEXT = "Twitch"
    DATABASE_CONTEXT = "Database"
    CONFIG_FILE = "scrappy_bot/resources/config.ini"

    client_id = None
    client_secret = None
    grant_type = None

    connection_string = None

    config = None

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)
        self._twitch_properties()
        self._database_properties()

    def _twitch_properties(self):
        self.set_client_id(self.config.get(self.TWITCH_CONTEXT, "client_id"))
        self.set_client_secret(self.config.get(self.TWITCH_CONTEXT, "client_secret"))
        self.set_grant_type(self.config.get(self.TWITCH_CONTEXT, "grant_type"))

    def _database_properties(self):
        self.set_connection_string(self.config.get(self.DATABASE_CONTEXT, "mongodb_connection"))

    def get_connection_string(self):
        return self.connection_string

    def set_connection_string(self, connection_string):
        self.connection_string = connection_string

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
