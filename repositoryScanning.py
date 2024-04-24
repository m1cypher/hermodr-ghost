# https://docs.github.com/en/rest?apiVersion=2022-11-28

import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
from github import Github, Auth
import base64
from bs4 import BeautifulSoup

TV_PATH = "03 - Projects/Media Reviews/TV Shows"
MOVIE_PATH = "03 - Projects/Media Reviews/Movies"
BOOK_PATH = "03 - Projects/Media Reviews/Books"


load_dotenv()

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

auth = Auth.Token(GITHUB_API_KEY)
github = Github(auth=auth)
# for repo in g.get_user().get_repos():
#     print(repo.name)

review_dc = {
    "TV": {},
    "Movies": {},
    "Books": {}
}

tv_items = {
    "name": "",
    "path": "",
    "imdbId": "",
    "status": "",
}

movie_items = {
    "name": "",
    "path": "",
    "imdbId": "",
    "status": "",
}

book_items = {
    "name": "",
    "path": "",
    "isbnId": "",
    "status": "",
}

tv_review_old = []

content_repo = github.get_user().get_repo("obsidian-notes")
contents = content_repo.get_contents(f"{TV_PATH}")
# print(contents[0])
for content_file in contents:
    tv_review_old.append(f"{content_file}")
# pprint(tv_review_old)    
for item in tv_review_old:
    new_item = item.replace("ContentFile(path=", '').replace(f'"{TV_PATH}/', '').replace('.md")', '')
    new_item_path = item.replace("ContentFile(path=", '').replace('.md")', '')
    review_dc["TV"][new_item] = tv_items.copy()
    review_dc["TV"][new_item]["name"] = new_item
    review_dc["TV"][new_item]["path"] = new_item_path

# pprint(review_dc)

for review_file in review_dc["TV"]:
    file_content = content_repo.get_contents(f"{TV_PATH}/{review_file}.md")
    content = file_content.content
    cleantext = base64.b64decode(content)
    cleantext = cleantext.decode("utf-8")
    cleantext.replace("\\n", "\n")
    cleantext = BeautifulSoup(cleantext, "lxml").text
    for line in cleantext.split('\n'):
        status_index = line.find("status: ")
        if status_index != -1:
            status = line[status_index + len("status: "):].strip()
            review_dc["TV"][review_file]["status"] = status

pprint(review_dc)

    # if "status: complete" in cleantext:
    #     print(f"{review_file} Completed review")
    # else:
    #     print(f"{review_file} This is not ready")

# pprint(review_dc)

