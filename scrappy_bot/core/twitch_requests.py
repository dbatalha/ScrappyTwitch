import requests
from scrappy_bot.core.properties_reader import PropertiesReader


def _do_http_request(url, payload, headers, method):
    return requests.request(method, url, headers=headers, data=payload)


class TwitchRequests:
    token = None
    properties = None
    helix_login = "https://id.twitch.tv/oauth2/token"
    helix_users = "https://api.twitch.tv/helix/users"
    helix_streams = "https://api.twitch.tv/helix/streams"

    login_object = None
    user_object = None
    stream_object = None

    def __init__(self, login_object, user_object, stream_object):
        self.properties = PropertiesReader()
        self.login_object = login_object
        self.user_object = user_object
        self.stream_object = stream_object

    def login(self):
        client_id = self.properties.get_client_id()
        client_secret = self.properties.get_client_secret()
        grant_type = self.properties.get_grant_type()

        payload = "client_id={}&client_secret={}&grant_type={}"
        payload = payload.format(client_id, client_secret, grant_type)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = _do_http_request(self.helix_login, payload, headers, "POST")
        if response.status_code == 200:
            self.login_object.parse_login(response.text)
            self.login_object.set_client_id(client_id)
            return True
        else:
            return False

    def users(self, streamer):
        self.helix_users = "{}{}{}".format(self.helix_users, "?login=", streamer)

        payload = {}
        headers = {
            'Client-Id': '{}'.format(self.login_object.get_client_id()),
            'Authorization': 'Bearer {}'.format(self.login_object.get_access_token())
        }

        response = _do_http_request(self.helix_users, payload, headers, "GET")
        if response.status_code == 200:
            self.user_object.parse_user(response.text)
            return True
        else:
            return False

    def streams(self, streamer_id):
        self.helix_streams = "{}{}{}".format(self.helix_streams, "?user_id=", streamer_id)

        payload = {}
        headers = {
            'Client-Id': '{}'.format(self.login_object.get_client_id()),
            'Authorization': 'Bearer {}'.format(self.login_object.get_access_token())
        }

        response = _do_http_request(self.helix_streams, payload, headers, "GET")
        if response.status_code == 200:
            self.stream_object.parse_stream(response.text)
            return True
        else:
            return False
