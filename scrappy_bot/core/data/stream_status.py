import json


class StreamStatus:
    stream = None
    status = None

    def get_stream(self):
        return self.stream

    def set_stream(self, stream):
        self.stream = stream

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def parse_login(self, json_string):
        json_login = json.loads(json_string)
        self.set_stream(json_login["stream"])
        self.set_status(json_login["status"])

    def to_json(self):
        stream_status_dict = {
            "stream": self.stream,
            "status": self.status
        }

        return json.dumps(stream_status_dict)
