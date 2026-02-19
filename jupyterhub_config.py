import sys
sys.path.insert(0, "/srv/jupyterhub")

from my_authenticator import SimpleAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

# jupyterhub_config.py
c = get_config()  # required to make JupyterHub recognize the file


# Use your custom authenticator
c.JupyterHub.authenticator_class = SimpleAuthenticator
# Bind to port 8000
c.JupyterHub.bind_url = "http://0.0.0.0:8000"


# Only allow specific users
c.Authenticator.allowed_users = {"testuser","user1"}

# Use safe dev spawner
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner
c.Spawner.cmd = ["jupyterhub-singleuser"]



c.Spawner.ip = "127.0.0.1"
c.Spawner.http_timeout = 60
c.Spawner.start_timeout = 60

