import json


class Stream:
    _id = None
    stream_status = None
    stream_id = None
    user_id = None
    user_login = None
    user_name = None
    game_id = None
    game_name = None
    title = None
    viewer_count = None
    started_at = None
    language = None
    thumbnail_url = None
    tag_ids = []
    tags = []
    is_mature = None

    def get_id(self):
        return self._id

    def set_id(self, stream_id):
        self._id = stream_id

    def get_stream_status(self):
        return self.stream_status

    def set_stream_status(self, stream_status):
        self.stream_status = stream_status

    def get_stream_id(self):
        return self.stream_id

    def set_stream_id(self, stream_id):
        self.stream_id = stream_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_login(self):
        return self.user_login

    def set_user_login(self, user_login):
        self.user_login = user_login

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_game_id(self):
        return self.game_id

    def set_game_id(self, game_id):
        self.game_id = game_id

    def get_game_name(self):
        return self.game_name

    def set_game_name(self, game_name):
        self.game_name = game_name

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_viewer_count(self):
        return self.viewer_count

    def set_viewer_count(self, viewer_count):
        self.viewer_count = viewer_count

    def get_started_at(self):
        return self.started_at

    def set_started_at(self, started_at):
        self.started_at = started_at

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def get_thumbnail_url(self):
        return self.thumbnail_url

    def set_thumbnail_url(self, thumbnail_url):
        self.thumbnail_url = thumbnail_url

    def get_tag_ids(self):
        return self.tag_ids

    def set_tag_ids(self, tag_ids):
        self.tag_ids = tag_ids

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_is_mature(self):
        return self.is_mature

    def set_is_mature(self, is_mature):
        self.is_mature = is_mature

    def parse_stream(self, json_string):
        json_stream = json.loads(json_string)

        is_online = len(json_stream["data"])
        if is_online == 0:
            self.set_stream_status("Offline")
        else:
            self.set_stream_status("Online")
            self.set_id(json_stream["data"][0]["id"])
            self.set_stream_id(json_stream["data"][0]["id"])
            self.set_user_id(json_stream["data"][0]["user_id"])
            self.set_user_login(json_stream["data"][0]["user_login"])
            self.set_user_name(json_stream["data"][0]["user_name"])
            self.set_game_id(json_stream["data"][0]["game_id"])
            self.set_game_name(json_stream["data"][0]["game_name"])
            self.set_title(json_stream["data"][0]["title"])
            self.set_viewer_count(json_stream["data"][0]["viewer_count"])
            self.set_started_at(json_stream["data"][0]["started_at"])
            self.set_language(json_stream["data"][0]["language"])
            self.set_thumbnail_url(json_stream["data"][0]["thumbnail_url"])
            self.set_tag_ids(json_stream["data"][0]["tag_ids"])
            self.set_tags(json_stream["data"][0]["tags"])
            self.set_is_mature(json_stream["data"][0]["is_mature"])
