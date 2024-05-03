# https://tinydb.readthedocs.io/
import os
from tinydb import TinyDB, Query
import re

class dataAccessor():
    def __init__(self):
        """
        Initializes the DataAccessor object.
        """
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/reviewdb.json")
        self.db = TinyDB(self.db_path)
        self.tv_show_table = self.db.table('tv_show')
        self.movie_table = self.db.table('movie')
        self.book_table = self.db.table('book')

    def initialize_db(self):
        """
        Initializes the database tables if the database file doesn't exist.
        """
        if not os.path.exists(self.db_path):
            self.db.purge_tables()

    def add_tv_show(self, name, path, status, imdb_id, date_published):
        """
        Adds a TV show to the database.

        Parameters:
            name (str): The name of the TV show.
            path (str): The path to the TV show.
            status (str): The status of the TV show (e.g., "Ongoing", "Finished").
            imdb_id (str): The IMDb ID of the TV show.
            date_published (str): The date the TV show was published (YYYY-MM-DD).

        Returns:
            int: The ID of the inserted TV show, or None if the TV show already exists.
        
        Example:
            data_accessor = DataAccessor()
            data_accessor.initialize_db()
            tv_show_id = data_accessor.add_tv_show("Breaking Bad", "/path/to/breaking_bad", "Ongoing", "tt0903747", "2008-01-20")
        """
        query = Query()
        if not self.tv_show_table.search(query.name == name):
            tv_show = {
                "name": name,
                "type": "TV",
                "path": path,
                "status": status,
                "imdbId": imdb_id,
                "date_published": date_published
            }
            self.tv_show_table.insert(tv_show)
            return f"Success: '{name}' was added to the DB."
        else:
            return f"Error: '{name}' is already in the DB."

    def add_movie(self, name, path, status, imdb_id, date_published):
        """
        Adds a movie to the database.

        Parameters:
            name (str): The name of the movie.
            path (str): The path to the movie.
            status (str): The status of the movie (e.g., "Released", "Upcoming").
            imdb_id (str): The IMDb ID of the movie.
            date_published (str): The date the movie was published (YYYY-MM-DD).

        Returns:
            int: The ID of the inserted movie, or None if the movie already exists.
        
        Example:
            data_accessor = DataAccessor()
            data_accessor.initialize_db()
            movie_id = data_accessor.add_movie("Inception", "/path/to/inception", "Released", "tt1375666", "2010-07-22")
        """
        query = Query()
        if not self.movie_table.search(query.name == name):
            movie = {
                "name": name,
                "type": "Movie",
                "path": path,
                "status": status,
                "imdbId": imdb_id,
                "date_published": date_published
            }
            self.movie_table.insert(movie)
            return f"Success: '{name}' was added to the DB."
        else:
            return f"Error: '{name}' is already in the DB."

    def add_book(self, name, path, status, isbn, date_published):
        """
        Adds a book to the database.

        Parameters:
            name (str): The name of the book.
            path (str): The path to the book.
            status (str): The status of the book (e.g., "Published", "Unpublished").
            isbn (str): The ISBN of the book.
            date_published (str): The date the book was published (YYYY-MM-DD).

        Returns:
            int: The ID of the inserted book, or None if the book already exists.
        
        Example:
            data_accessor = DataAccessor()
            data_accessor.initialize_db()
            book_id = data_accessor.add_book("The Hobbit", "/path/to/hobbit", "Published", "978-0261102217", "1937-09-21")
        """
        query = Query()
        if not self.book_table.search(query.name == name):
            book = {
                "name": name,
                "type": "Book",
                "path": path,
                "status": status,
                "isbn": isbn,
                "date_published": date_published
            }
            self.book_table.insert(book)
            return f"Success: '{name}' was added to the DB."
        else:
            return f"Error: '{name}' is already in the DB."

    def delete_item_by_id(self, item_type, item_id):
        """
        Deletes an item from the database by ID.

        Parameters:
            item_type (str): The type of item to delete ("tv_show", "movie", or "book").
            item_id (int): The ID of the item to delete.

        Returns:
            bool: True if the item is successfully deleted, False otherwise.
        
        Example:
            data_accessor = DataAccessor()
            deleted = data_accessor.delete_item_by_id("tv_show", tv_show_id)
        """
        table = None
        if item_type == "tv_show":
            table = self.tv_show_table
        elif item_type == "movie":
            table = self.movie_table
        elif item_type == "book":
            table = self.book_table

        if table:
            table.remove(doc_ids=[item_id])
            return True
        else:
            return False

    def update_item_by_id(self, item_type, item_id, new_data):
        """
        Updates an item in the database by ID.

        Parameters:
            item_type (str): The type of item to update ("tv_show", "movie", or "book").
            item_id (int): The ID of the item to update.
            new_data (dict): The new data to update the item with.

        Returns:
            bool: True if the item is successfully updated, False otherwise.
        
        Example:
            data_accessor = DataAccessor()
            updated = data_accessor.update_item_by_id("tv_show", tv_show_id, {"status": "Finished"})
        """
        table = None
        if item_type == "tv_show":
            table = self.tv_show_table
        elif item_type == "movie":
            table = self.movie_table
        elif item_type == "book":
            table = self.book_table

        if table:
            table.update(new_data, doc_ids=[item_id])
            return True
        else:
            return False

    def search_item(self, key, value):
        """
        Searches for an item in the database.

        Parameters:
            key (str): The type of item to search for ("tv_show", "movie", or "book").
            value (str): The value to search for.

        Returns:
            int: The ID of the first item found, or None if no item is found.
        
        Example:
            data_accessor = DataAccessor()
            tv_show_id = data_accessor.search_item("tv_show", "Breaking Bad")
        """
        if key == "tv_show":
            table = self.tv_show_table
        elif key == "movie":
            table = self.movie_table
        elif key == "book":
            table = self.book_table
        else:
            return None

        query = Query()
        result = table.search(query.name.search(value, flags=re.IGNORECASE))
        if result:
            return result[0]
        else:
            return None
    