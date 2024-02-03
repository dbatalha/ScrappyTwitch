from scrappy_bot.core.presistance.mongodb_client import MongoDBClient
from scrappy_bot.core.properties_reader import PropertiesReader


class StreamsFlow:
    STREAMS = "Streams"
    DATABASE = "Scrappy"

    mongodb_client = None

    def __init__(self):
        properties = PropertiesReader()
        self.mongodb_client = MongoDBClient(properties.get_connection_string())

    def _stream_setup(self):
        self.mongodb_client.set_database(self.DATABASE)
        self.mongodb_client.set_collection(self.STREAMS)

    def create_stream(self, stream, stream_name):
        self._stream_setup()

        found_stream = self.mongodb_client.find_one_element("user_name", stream_name)

        if stream.get_stream_status() == "Offline" and found_stream:
            self.delete_stream("user_name", stream_name)

        if stream.get_stream_status() == "Offline":
            return

        found_document = self.mongodb_client.find_one_element("_id", stream.get_id())
        if found_document:
            self.update_stream(stream.get_id(), stream)
        else:
            self.mongodb_client.insert_one_collection(stream)

    def update_stream(self, qfilter, stream):
        self._stream_setup()

        query_filter = {'_id': qfilter}
        update_data = {'$set': stream.__dict__}

        self.mongodb_client.update_one_collection(query_filter, update_data)

    def delete_stream(self, key, value):
        self._stream_setup()

        self.mongodb_client.delete_one(key, value)
