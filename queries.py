import sqlite3
from word import Word

class Queries:
    """Class containing queries to be used in the app as staticmethods."""

    @staticmethod
    def setup_db() -> None:
        """Creates the words table in the db if it does not exist yet."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS categories (category TEXT PRIMARY KEY NOT NULL UNIQUE)""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                hungarian TEXT NOT NULL,
                                                                english TEXT NOT NULL,
                                                                danish TEXT NOT NULL,
                                                                category TEXT REFERENCES categories(category) ON DELETE CASCADE)""")
            conn.commit()


    @staticmethod
    def get_all_words() -> list:
        """Fetches all words from the db and returns a list of Word objects."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM words")
            word_list = cursor.fetchall()
        words = [Word(*word) for word in word_list]
        return words


    @staticmethod
    def get_all_categories() -> list:
        """Fetches all categories from the db and returns them as a list."""
        with sqlite3.Connection('words.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categories")
            categories = cursor.fetchall()
        return [category[0] for category in categories]
    

    @staticmethod
    def add_category(received_data: str) -> None:
        """Adds the category into the db."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            print("RECEIVED DATA", received_data)
            cursor.execute("INSERT INTO categories (category) VALUES (?)", (received_data,))
            conn.commit()
    

    @staticmethod
    def delete_category(category_to_delete: str) -> None:
        """Deletes the category from the db and all words corresponding to it."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM words WHERE category = ?", (category_to_delete,))
            cursor.execute("DELETE FROM categories WHERE category = ?", (category_to_delete,))


    @staticmethod
    def add_word(received_data: tuple) -> None:
        """Adds the tuple containing the word into the db."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO words (hungarian, english, danish, category) VALUES (?,?,?,?)", received_data)
            conn.commit()


    @staticmethod
    def delete_word(id_to_delete: int) -> None:
        """"Deletes the word from the db with the given id."""
        with sqlite3.Connection("words.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM words WHERE id = ?", (id_to_delete,))
            conn.commit()
