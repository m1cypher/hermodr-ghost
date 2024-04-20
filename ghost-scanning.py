import requests
import os
from dotenv import load_dotenv

load_dotenv()



GHOST_BLOG_URL = os.getenv("GHOST_BLOG")

response = requests.get(GHOST_BLOG_URL)
