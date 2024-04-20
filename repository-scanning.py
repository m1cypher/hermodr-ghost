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

tv_review_old = []
tv_reviews_dictionary = {}

content_repo = github.get_user().get_repo("obsidian-notes")
contents = content_repo.get_contents(f"{TV_PATH}")
for content_file in contents:
    tv_review_old.append(f"{content_file}")
# pprint(tv_review_old)    
for item in tv_review_old:
    new_item = item.replace("ContentFile(path=", '')
    new_item = new_item.replace(f'"{TV_PATH}/', '')
    new_item = new_item.replace('.md")', '')
    tv_reviews_dictionary[new_item] = ''
print(tv_reviews_dictionary)

for review_file in tv_reviews_dictionary:
    file_content = content_repo.get_contents(f"{TV_PATH}/{review_file}.md")
    content = file_content.content
    cleantext = base64.b64decode(content)
    cleantext.replace('\\n', "\n")
    # cleantext = BeautifulSoup(cleantext, "lxml").text

    # for line in cleantext:
    #     print(line)

    # if "status: complete" in cleantext:
    #     print("Completed review")
    # else:
    #     print("This is not ready")

# pprint(review_dictionary)

