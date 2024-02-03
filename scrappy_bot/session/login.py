import json


class Login:
    access_token = None
    expires_in = None
    token_type = None
    client_id = None

    def get_access_token(self):
        return self.access_token
    
    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_expires_in(self):
        return self.expires_in
    
    def set_expires_in(self, expires_in):
        self.expires_in = expires_in

    def get_token_type(self):
        return self.token_type
    
    def set_token_type(self, token_type):
        self.token_type = token_type

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id

    def parse_login(self, json_string):
        json_login = json.loads(json_string)
        self.set_access_token(json_login["access_token"])
        self.set_expires_in(json_login["expires_in"])
        self.set_token_type(json_login["token_type"])
