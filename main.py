import sqlite3
class DatabaseManager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                requested_film1 TEXT
                requested_film2 TEXT
                requested_film3 TEXT
            )
        ''')
            conn.execute('''
            CREATE TABLE IF NOT EXISTS requested movies (
                user_id INTEGER PRIMARY KEY,
                requested_film1 TEXT
                requested_film2 TEXT
                requested_film3 TEXT
            )
        ''')
    def add_user(self, user_id, film1, film2, film3):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('INSERT INTO requested_films VALUES (?, ?, ?, ?)', (user_id, film1, film2, film3))
            conn.commit()