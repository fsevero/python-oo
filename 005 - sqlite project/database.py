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

    def make_schema(self):
        """Created database tables"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                document TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL
            );
            """)
        except AttributeError:
            print('There are no database connection present')

    def insert_client(self, name, document, email):
        """Insert a new client in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            INSERT INTO clients (name, document, email) VALUES (?, ?, ?)
            """, (name, document, email))
            self.connection.commit()
        except AttributeError:
            print('There are no database connection present')
        except sqlite3.IntegrityError:
            print('Document {} already exists. Cannot duplicate'.format(document))