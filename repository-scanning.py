# https://docs.github.com/en/rest?apiVersion=2022-11-28

import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
from github import Github, Auth
import base64
from bs4 import BeautifulSoup



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
# print(content_data)

review_dictionary = {}

for review in content_data:
    review_name = review['name']
    review_path = review['path']
    review_dictionary[review_name.strip('.md')] = {'name': review_name, 'path': review_path}


# Working to pull commit time, but only shows entire repo. Wanted specific file. See #Content-frontmatter for attempted new direction.
# commit_response = requests.get(url=GITHUB_REPO_PATH_COMMITS, headers=HEADERS)
# commit_response.raise_for_status()

# commit_data = commit_response.json()
# # review_dictionary[review_name.strip('.md')]
# # print(commit_data[0]['commit']['committer']['date'])
# pprint(commit_data)

auth = Auth.Token(GITHUB_API_KEY)
github = Github(auth=auth)
# for repo in g.get_user().get_repos():
#     print(repo.name)

content_repo = github.get_user().get_repo("obsidian-notes")
file_content = content_repo.get_contents("03 - Projects/Media Reviews/TV Shows/Brooklyn Nine-Nine.md")
content = file_content.content
cleantext = BeautifulSoup(base64.b64decode(content), "lxml").text

if "status: complete" in cleantext:
    print("Completed review")
else:
    print("This is not ready")

# pprint(review_dictionary)

