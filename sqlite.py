import sqlite3
import os
from hashlib import sha256


class Database:
    _DATABASE_NAME = "timesheet.db"

    def __init__(self):
        self._connection = None
        self.main_cursor = None
        is_present = os.path.isfile(self._DATABASE_NAME)
        self.connect()
        if not is_present:
            self._create_schema()
        if not self._check_schema():
            raise sqlite3.Error("База данных повреждена")

    def connect(self):
        try:
            self._connection = sqlite3.connect(self._DATABASE_NAME)
            self.main_cursor = self._connection.cursor()
        except sqlite3.Error as err:
            self.disconnect()
            raise err

    def disconnect(self):
        if self._connection:
            self._connection.close()
        self.main_cursor = None

    def _check_schema(self):
        result = self.main_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_data'")
        return len(result.fetchone()) > 0

    def _create_schema(self):
        self.main_cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
        login TEXT,
        password TEXT,
        role TEXT
        )''')
        self.main_cursor.execute(f"INSERT INTO user_data(login, password, role) VALUES('admin', "
                                 f"'{sha256('admin'.encode('utf-8')).hexdigest()}', 'admin')")
        self._connection.commit()

    def authenticate(self, login, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        result = self.main_cursor.execute("SELECT role FROM user_data WHERE login = ? AND password = ?", (login, password))
        result = result.fetchone()
        if not result:
            return None
        return result[0]