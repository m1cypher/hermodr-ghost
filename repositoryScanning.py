# https://docs.github.com/en/rest?apiVersion=2022-11-28

import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime
from github import Github, Auth
import base64
from bs4 import BeautifulSoup
import json

load_dotenv()

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

auth = Auth.Token(GITHUB_API_KEY)
github = Github(auth=auth)
# for repo in g.get_user().get_repos():
#     print(repo.name)

def fetch_content(repo_name, folder_path):
    content_repo = github.get_user().get_repo(repo_name) # was "obsidian-notes"
    contents = content_repo.get_contents(folder_path) # was f"{TV_PATH}"
    return [content_file.path for content_file in contents]

def extract_review_details(review, file_path):
    name = review.replace(f'"{file_path}/', '').replace('.md")', '')
    name = name.split("/")[-1].replace('.md', '')
    path = review.replace('.md")', '')
    # path = path.split("/")[-1].replace('.md', '')
    return name, path

def update_tv_review_status(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            status_index = line.find("status: ")
            if status_index != -1:
                status = line[status_index + len("status: "):].strip()
                review_dc[review_file]["status"] = status    
    return review_dc

def update_tv_imdb_info(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            status_index = line.find("imbdId: ")
            if status_index != -1:
                imdbId = line[status_index + len("imdbId: "):].strip()
                review_dc[review_file]['imdbId'] = imdbId
    return review_dc


def update_movie_review_status(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            status_index = line.find("status: ")
            if status_index != -1:
                status = line[status_index + len("status: "):].strip()
                review_dc[review_file]["status"] = status
    return review_dc

def update_movie_imdb_info(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            status_index = line.find("imbdId: ")
            if status_index != -1:
                imdbId = line[status_index + len("imdbId: "):].strip()
                review_dc[review_file]['imdbId'] = imdbId
    return review_dc

def update_book_review_status(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            status_index = line.find("status: ")
            if status_index != -1:
                status = line[status_index + len("status: "):].strip()
                review_dc[review_file]["status"] = status
    return review_dc

def update_book_isbn_info(review_dc, repo_name, file_path):
    content_repo = github.get_user().get_repo(repo_name)
    for review_file in review_dc:
        file_content = content_repo.get_contents(f"{file_path}/{review_file}.md")
        content = file_content.content
        cleantext = base64.b64decode(content).decode("utf-8")
        cleantext = BeautifulSoup(cleantext, "lxml").text
        for line in cleantext.split('\n'):
            isbn_index = line.find("isbn: ")
            if isbn_index != -1:
                isbn = line[isbn_index + len("isbn: "):].strip()
                review_dc[review_file]['isbn'] = isbn
    return review_dc


def main():
    TV_PATH = "03 - Projects/Media Reviews/TV Shows"
    MOVIE_PATH = "03 - Projects/Media Reviews/Movies"
    BOOK_PATH = "03 - Projects/Media Reviews/Books"

    review_dc = {"TV": {}, "Movies": {},"Books": {}}



    # TV Information Gathering
    tv_review_old = fetch_content('obsidian-notes', TV_PATH)
    for review in tv_review_old:
        name, path = extract_review_details(review, TV_PATH)
        if name not in review_dc["TV"]:
            review_dc["TV"][name] = {
                "name": name,
                "path": path,
                "imdbId": "",
                "status": ""
            }

    review_dc["TV"] = update_tv_review_status(review_dc["TV"], "obsidian-notes", TV_PATH)
    review_dc["TV"] = update_tv_imdb_info(review_dc["TV"], "obsidian-notes", TV_PATH)

    # Movie Information Gathering
    # movie_review_old = fetch_content("obsidian-notes", MOVIE_PATH)

    # for review in movie_review_old:
    #     name, path = extract_review_details(review, MOVIE_PATH)
    #     if name not in review_dc["Movies"]:
    #         review_dc["Movies"][name] = {
    #             "name": name,
    #             "path": path,
    #             "imdbId": "",
    #             "status": ""
    #         }

    # review_dc["Movies"] = update_movie_review_status(review_dc["Movies"], 'obsidian-notes', MOVIE_PATH)
    # review_dc["Movies"] = update_movie_imdb_info(review_dc["Movies"], 'obsidian-notes', MOVIE_PATH)

    # # Book Information Gathering
    # book_review_old = fetch_content("obsidian-notes", BOOK_PATH)

    # for item in book_review_old:
    #     name, path = extract_review_details(item, BOOK_PATH)
    #     if name not in review_dc["Books"]:
    #         review_dc["Books"][name] = {
    #             "name": name,
    #             "path": path,
    #             "isbnId": "",
    #             "status": ""
    #         }

    # review_dc["Books"] = update_book_review_status(review_dc["Books"], "obsidian-notes", BOOK_PATH)
    # review_dc["Books"] = update_book_isbn_info(review_dc["Books"], 'obsidian-notes', BOOK_PATH)

    pprint(review_dc)
