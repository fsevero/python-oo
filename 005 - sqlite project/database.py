import sqlite3

class Database:
    """Represents the project database"""

    def __init__(self, database_name="database.sqlite3"):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        """Connects to the database file"""
        self.connection = sqlite3.connect(self.database_name)

    def disconnect(self):
        """Disconnects from the database file"""
        try:
            self.connection.close()
        except AttributeError:
            pass