import os
import logging
from dotenv import load_dotenv
from pprint import pprint

from ghostAdmin import GhostAdmin
from repositoryScanning import GithubReviewAdmin


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='hermodr.log'
)

def main():
    load_dotenv()
    GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

    updater = GithubReviewAdmin(GITHUB_API_KEY)

    tv_accessor = updater.process_reviews("TV Shows", "TV")
    movie_accessor = updater.process_reviews("Movies", "Movie")
    book_accessor = updater.process_reviews("Books", "Book")

    review_dc = {"TV": tv_accessor, "Movies": movie_accessor, "Books": book_accessor}
    pprint(review_dc)

if __name__ == "__main__":
    main()