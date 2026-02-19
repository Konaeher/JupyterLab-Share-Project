from jupyterhub.auth import Authenticator
from tornado import gen

class SimpleAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        username = data.get("username")
        password = data.get("password")

        if username == "testuser" and password == "password":
            return username
        return None
