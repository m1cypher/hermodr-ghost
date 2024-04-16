import requests
from io import StringIO
import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime




load_dotenv()

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

HEADERS = headers={
        'Accept': 'application/vnd.github.v3.raw',
        'Authorization': f'Bearer {GITHUB_API_KEY}',
        'X-GitHub-Api-Version': '2022-11-28'
            }

GITHUB_REPO_PATH_CONTENTS = "https://api.github.com/repos/m1cypher/obsidian-notes/contents/03%20-%20Projects/Media%20Reviews/TV%20Shows/"
GITHUB_REPO_PATH_COMMITS = "https://api.github.com/repos/m1cypher/obsidian-notes/commits?path=03%20-%20Projects/Media%20Reviews/TV%20Shows/"

content_response = requests.get(url=GITHUB_REPO_PATH_CONTENTS, headers=HEADERS)
content_response.raise_for_status()

content_data = content_response.json()

review_dictionary = {}

for review in content_data:
    review_name = review['name']
    review_path = review['path']
    review_dictionary[review_name.strip('.md')] = {'name': review_name, 'path': review_path}

commit_response = requests.get(url=GITHUB_REPO_PATH_COMMITS, headers=HEADERS)
commit_response.raise_for_status()

commit_data = commit_response.json()

for commit in commit_data:
    print(commit['commit']['committer']['date'])


# pprint(review_dictionary)

