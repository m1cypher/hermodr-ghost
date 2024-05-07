import os
import logging
from dotenv import load_dotenv
from pprint import pprint

from ghostAdmin import GhostAdmin
from repositoryScanning import GithubReviewAdmin
from dataAccessor import dataAccessor
from imageProcessing import ImageOverlay


# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     filename= os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/hermodr.log')
# )


# def get_content():
#     GithubReviewAdmin.fetch_content

def main():
    load_dotenv()
    GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

    da = dataAccessor()
    da.initialize_db()

    gra = GithubReviewAdmin(GITHUB_API_KEY)


    
    # ga = GhostAdmin()
    # img = ImageOverlay()

    gra.process_reviews("TV Shows", "tv")
    # movie_accessor = gra.process_reviews("Movies", "movie")
    # book_accessor = gra.process_reviews("Books", "book")

if __name__ == "__main__":
    main()


