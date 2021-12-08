import sqlite3
import os
from hashlib import sha256

import data_models


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
        self.main_cursor.execute(f"INSERT INTO user_data(login, password, role) VALUES('laborant', "
                                 f"'{sha256('laborant'.encode('utf-8')).hexdigest()}', 'laborant')")
        self._connection.commit()

    def authenticate(self, login, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        result = self.main_cursor.execute("SELECT role FROM user_data WHERE login = ? AND password = ?", (login, password))
        result = result.fetchone()
        if not result:
            return None
        return result[0]

# TODO: Подгрузки данных
    def load_rooms(self):
        rooms = []
        result = self.main_cursor.execute("SELECT rooms.id, campus, number, room_types.name FROM rooms "
                                          "LEFT JOIN room_types ON rooms.id = room_types.id")
        for row in result:
            rooms.append(data_models.Room(result[0], result[1], result[2], result[3]))
        return rooms

    def add_room(self, room):
        result = self.main_cursor.execute("SELECT id FROM room_types WHERE name = ?", room.type)
        result = result.fetchone()
        if len(result) != 1:
            raise sqlite3.Error("Внутренняя ошибка базы данных")
        self.main_cursor.execute(f"INSERT INTO rooms(id, campus, number, type) VALUES(?, ?, ?, ?)",
                                 room.id, room.campus, room.number, room.type)
        self._connection.commit()

    def load_personals(self):
        personals = []
        result = self.main_cursor.execute("SELECT  id, name, surname, patronymic, email, phone, photo "
                                          "FROM personal_data")
        for row in result:
            personals.append(data_models.Room(result[0], result[1], result[2], result[3],
                                              result[4], result[5], result[6]))
        return personals

    def add_personal(self, personal_data):
        self.main_cursor.execute(f"INSERT INTO personal_data(name, surname, patronymic, email, phone, photo) VALUES(?, ?, ?, ?)",
                                 personal_data.name, personal_data.surname, personal_data.patronymic,
                                 personal_data.email, personal_data.phone, personal_data.photo)
        self._connection.commit()
