import json
import requests
from scrappy_bot.core.properties_reader import PropertiesReader


class WatchGateway:
    properties = None

    def __init__(self):
        self.properties = PropertiesReader()

    def add_watcher(self, watcher):
        payload = json.dumps(watcher.to_json())
        headers = {
            'Content-Type': 'application/json'
        }

        return requests.request("POST",
                                "{}/{}".format(self.properties.get_persistence_url(),
                                               "watcher"),
                                headers=headers,
                                data=payload)

    def get_all_watchers(self):
        payload = {}
        headers = {}

        response = requests.request("GET",
                                    "{}/{}".format(self.properties.get_persistence_url(),
                                                   "watchers"),
                                    headers=headers,
                                    data=payload)
        if response.text is not None:
            response_string = json.loads(response.text)
            return response_string["watchers"]
