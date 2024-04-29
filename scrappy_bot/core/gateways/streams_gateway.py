import json
import requests

from scrappy_bot.core.properties_reader import PropertiesReader


class StreamsGateway:
    def __init__(self):
        self.properties = PropertiesReader()

    def create_stream(self, stream):
        payload = json.dumps(stream.to_json())
        headers = {
            'Content-Type': 'application/json'
        }

        if stream.get_id() is None:
            return

        return requests.request("POST",
                                "{}/{}".format(self.properties.get_persistence_url(),
                                               "stream".format()),
                                headers=headers,
                                data=payload)

    def update_stream(self, stream):
        payload = json.dumps(stream.to_json())
        headers = {
            'Content-Type': 'application/json'
        }

        if stream.get_id() is None:
            return

        return requests.request("PUT",
                                "{}/{}".format(self.properties.get_persistence_url(),
                                               "stream".format()),
                                headers=headers,
                                data=payload)

    def delete_stream(self, stream_name):
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }

        if stream_name is None:
            return

        return requests.request("DELETE",
                                "{}/{}?user_name={}".format(self.properties.get_persistence_url(),
                                                            "stream".format(), stream_name),
                                headers=headers,
                                data=payload)
