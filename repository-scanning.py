import requests
from io import StringIO
import os


GITHUB_REPO_API = os.getenv("GITHUB_API_KEY")

HEADERS = headers={
        'accept': 'application/vnd.github.v3.raw',
        'authorization': 'token {}'.format(token)
            }