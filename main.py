import os
import logging
from dotenv import load_dotenv

from ghostAdmin import GhostAdmin  


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='hermodr.log'
)


GhostAdmin.getMembers()