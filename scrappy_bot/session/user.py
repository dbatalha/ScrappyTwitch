import json


class User:
    _id = None
    user_id = None
    login = None
    display_name = None
    broadcaster_type = None
    description = None
    profile_image_url = None
    offline_image_url = None
    created_at = None

    def get_id(self):
        return self._id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_display_name(self):
        return self.display_name

    def set_display_name(self, display_name):
        self.display_name = display_name

    def get_broadcaster_type(self):
        return self.broadcaster_type

    def set_broadcaster_type(self, broadcaster_type):
        self.broadcaster_type = broadcaster_type

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_profile_image_url(self):
        return self.profile_image_url

    def set_profile_image_url(self, profile_image_url):
        self.profile_image_url = profile_image_url

    def get_offline_image_url(self):
        return self.offline_image_url

    def set_offline_image_url(self, offline_image_url):
        self.offline_image_url = offline_image_url

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def parse_user(self, json_string):
        json_user = json.loads(json_string)
        self.set_user_id(json_user["data"][0]["id"])
        self.set_login(json_user["data"][0]["login"])
        self.set_display_name(json_user["data"][0]["display_name"])
        self.set_broadcaster_type(json_user["data"][0]["broadcaster_type"])
        self.set_description(json_user["data"][0]["description"])
        self.set_profile_image_url(json_user["data"][0]["profile_image_url"])
        self.set_offline_image_url(json_user["data"][0]["offline_image_url"])
        self.set_created_at(json_user["data"][0]["created_at"])
        self._id = self.get_user_id()
