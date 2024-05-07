# https://docs.github.com/en/rest?apiVersion=2022-11-28

from datetime import datetime
from github import Github, Auth
import base64
from bs4 import BeautifulSoup
from dataAccessor import dataAccessor



class GithubReviewAdmin:
    
    def __init__(self, github_api_key):
        self.github_api_key = github_api_key
        self.github = self._authenticate()

    def _authenticate(self):
        auth = Auth.Token(self.github_api_key)
        return Github(auth=auth)

    def fetch_content(self, repo_name, folder_path):
        content_repo = self.github.get_user().get_repo(repo_name)
        contents = content_repo.get_contents(folder_path)
        return [content_file.path for content_file in contents]

    def extract_review_details(self, review, file_path):
        name = review.replace(f'"{file_path}/', '').replace('.md")', '')
        name = name.split("/")[-1].replace('.md', '')
        path = review.replace('.md")', '')
        return name, path

    def update_review_status(self, accessor, repo_name, file_path, key, value):
        content_repo = self.github.get_user().get_repo(repo_name)
        print(content_repo)
        review_files = accessor.search_item("name", value)
        if review_files:
            for review_file in review_files:
                file_content = content_repo.get_contents(f"{file_path}/{review_file['path']}.md")
                content = file_content.content
                cleantext = base64.b64decode(content).decode("utf-8")
                cleantext = BeautifulSoup(cleantext, "lxml").text
                for line in cleantext.split('\n'):
                    status_index = line.find(f"{key}: ")
                    if status_index != -1:
                        status = line[status_index + len(f"{key}: "):].strip()
                        accessor.update_item_by_id(review_file['type'], review_file.doc_id, {"status": status})
        else:
            print(f"No {value} found.")

    def update_imdb_info(self, accessor, repo_name, file_path, key, value):
        content_repo = self.github.get_user().get_repo(repo_name)
        review_files = accessor.search_item("name", value)
        if review_files:
            for review_file in review_files:
                file_content = content_repo.get_contents(f"{file_path}/{review_file['path']}.md")
                content = file_content.content
                cleantext = base64.b64decode(content).decode("utf-8")
                cleantext = BeautifulSoup(cleantext, "lxml").text
                for line in cleantext.split('\n'):
                    status_index = line.find(f"{key}: ")
                    if status_index != -1:
                        imdbId = line[status_index + len(f"{key}: "):].strip()
                        accessor.update_item_by_id(review_file['type'], review_file.doc_id, {"imdbId": imdbId})
        else:
            print(f"No {value} found.")

    def update_isbn_info(self, accessor, repo_name, file_path, key, value):
        content_repo = self.github.get_user().get_repo(repo_name)
        review_files = accessor.search_item("name", value)
        if review_files:
            for review_file in review_files:
                file_content = content_repo.get_contents(f"{file_path}/{review_file['path']}.md")
                content = file_content.content
                cleantext = base64.b64decode(content).decode("utf-8")
                cleantext = BeautifulSoup(cleantext, "lxml").text
                for line in cleantext.split('\n'):
                    isbn_index = line.find(f"{key}: ")
                    if isbn_index != -1:
                        isbn = line[isbn_index + len(f"{key}: "):].strip()
                        accessor.update_item_by_id(review_file['type'], review_file.doc_id, {"isbn": isbn})
        else:
            print(f"No {value} found.")

    def process_reviews(self, path, review_type):
        review_path = f"03 - Projects/Media Reviews/{path}"
        accessor = dataAccessor()
        review_old = self.fetch_content('obsidian-notes', review_path)
        for review in review_old:
            name, path = self.extract_review_details(review, review_path)
            if review_type == "tv":
                accessor.add_tv_show(name, path, "", "", "")
            elif review_type == "movie":
                accessor.add_movie(name, path, "", "", "")
            elif review_type == "book":
                accessor.add_book(name, path, "", "", "")
        self.update_review_status(accessor, "obsidian-notes", review_path, "status", "status")
        self.update_imdb_info(accessor, "obsidian-notes", review_path, "imbdId", "imdbId")
        self.update_isbn_info(accessor, "obsidian-notes", review_path, "isbn", "isbnId")
        return accessor

