import json
import requests

from scrappy_bot.core.properties_reader import PropertiesReader


class UsersGateway:
    properties = None

    def __init__(self):
        self.properties = PropertiesReader()

    def save_user(self, user):
        payload = json.dumps(user.to_json())
        headers = {
            'Content-Type': 'application/json'
        }

        return requests.request("POST",
                                "{}/{}".format(self.properties.get_persistence_url(),
                                               "user"),
                                headers=headers,
                                data=payload)
