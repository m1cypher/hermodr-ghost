# https://github.com/pysonDB/pysonDB
from pysondb import db
import os

class dataAccessor():
    """
    A class to interact with the database for storing TV shows, movies, and books reviews.
    """

    def __init__(self):
        """
        Initializes the DataAccessor object and creates or loads the database.
        """
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/reviewdb.json")
        self.create_or_load_db()

    def create_or_load_db(self):
        """
        Creates or loads the database.
        """
        if not os.path.exists(self.file_path):
            self.db = db.getDb(self.file_path)
            self.db.data = []
            self.db.commit()
        else:
            self.db = db.getDb(self.file_path)
        

    def add_tv_show(self, name, path, status, imdb_id, date_published):
        """
        Adds a TV show review to the database.

        Args:
            name (str): The name of the TV show.
            path (str): The path of the TV show.
            status (str): The status of the TV show (e.g., "Watching", "Finished").
            imdb_id (str): The IMDb ID of the TV show.
            date_published (str): The date the TV show was published.

        Returns:
            None
        """
        tv_show = {
            "type": "TV",
            "name": name,
            "path": path,
            "status": status,
            "imdbId": imdb_id,
            "date_published": date_published
        }
        self.db.data.append(tv_show)
        self.db.commit()

    def add_movie(self, name, path, status, imdb_id, date_published):
        """
        Adds a movie review to the database.

        Args:
            name (str): The name of the movie.
            path (str): The path of the movie.
            status (str): The status of the movie (e.g., "Watching", "Finished").
            imdb_id (str): The IMDb ID of the movie.
            date_published (str): The date the movie was published.

        Returns:
            None
        """
        movie = {
            "type": "Movie",
            "name": name,
            "path": path,
            "status": status,
            "imdbId": imdb_id,
            "date_published": date_published
        }
        self.db.data.append(movie)
        self.db.commit()
    
    def add_book(self, name, path, status, isbn, date_published):
        """
        Adds a book review to the database.

        Args:
            name (str): The name of the book.
            path (str): The path of the book.
            status (str): The status of the book (e.g., "Reading", "Finished").
            isbn (str): The ISBN of the book.
            date_published (str): The date the book was published.

        Returns:
            None
        """
        book = {
            "type": "Book",
            "name": name,
            "path": path,
            "status": status,
            "isbn": isbn,
            "date_published": date_published
        }
        self.db.data.append(book)
        self.db.commit()

    def delete_item_by_id(self, item_id):
        """
        Deletes an item from the database by its ID.

        Args:
            item_id (int): The ID of the item to be deleted.

        Returns:
            bool: True if the item is deleted successfully, False otherwise.
        """
        for item in self.db.data:
            if item["id"] == item_id:
                self.db.data.remove(item)
                self.db.commit()
                return True
        return False

    def update_item_by_id(self, item_id, new_data):
        """
        Updates an item in the database by its ID.

        Args:
            item_id (int): The ID of the item to be updated.
            new_data (dict): The new data for the item.

        Returns:
            bool: True if the item is updated successfully, False otherwise.
        """
        for item in self.db.data:
            if item["id"] == item_id:
                item.update(new_data)
                self.db.commit()
                return True
        return False
    
    def search(self, key, value):
        """
        Searches for items in the database by a specific key and value.

        Args:
            key (str): The key to search by.
            value (str): The value to search for.

        Returns:
            list: A list of items that match the search criteria.
        """
        results = []
        for item in self.db.data:
            if item.get(key) == value:
                results.append(item)
        return results
    
