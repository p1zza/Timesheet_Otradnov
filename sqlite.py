import sqlite3
import os
from hashlib import sha256

from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

import data_models


class AlreadyExistsError(sqlite3.Error):
    pass


class Database:
    # Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self, db_path="timesheet.db"):
        self._connection = None
        self.main_cursor = None
        self._database_path = db_path
        is_present = os.path.isfile(self._database_path)
        self.connect()
        if not is_present:
            self._create_schema()
        if not self._check_schema():
            raise sqlite3.Error("База данных повреждена")

    def connect(self):
        try:
            self._connection = sqlite3.connect(self._database_path)
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
        result = result.fetchone()
        return result and len(result) > 0

    def _create_schema(self):
        with open('schema.sql', 'r', encoding='utf-8') as file:
            schema = file.read()
        self.main_cursor.executescript(schema)
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
        result = self.main_cursor.execute("SELECT campus, number, room_types.type FROM rooms "
                                          "LEFT JOIN room_types ON rooms.type_id = room_types.id")
        result = result.fetchone()
        if not result:
            return rooms
        for row in result:
            rooms.append(data_models.Room(result[0], result[1], result[2]))
        return rooms

    def add_room(self, room):
        result = self.main_cursor.execute("SELECT id FROM room_types WHERE type = ?", (room.type.type,))
        result = result.fetchone()
        if len(result) != 1:
            raise sqlite3.Error("Внутренняя ошибка базы данных")
        result = self.main_cursor.execute("SELECT id FROM rooms WHERE campus = ? AND number = ?",
                                          (room.campus, room.number))
        result = result.fetchone()
        if result:
            raise AlreadyExistsError("Такая аудитория уже существует")
        self.main_cursor.execute(f"INSERT INTO rooms(campus, number, type_id) VALUES(?, ?, ?)",
                                 (room.campus, room.number, room.type.type))
        self._connection.commit()

    def add_room_type(self, room_type):
        result = self.main_cursor.execute("SELECT type FROM room_types WHERE type = ?", (room_type.type,))
        result = result.fetchone()
        if result:
            raise AlreadyExistsError("Такой тип аудитории уже существует")
        self.main_cursor.execute(f"INSERT INTO room_types (type) VALUES (?)", (room_type.type,))
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
        self.main_cursor.execute(f"INSERT INTO personal_data(name, surname, patronymic, email, phone, photo) VALUES(?, ?, ?, ?, ?, ?, ?)",
                                 personal_data.name, personal_data.surname, personal_data.patronymic,
                                 personal_data.email, personal_data.phone, personal_data.photo)
        self._connection.commit()

    def add_user(self,login,password,role):
        try:
            self.main_cursor.execute(f"INSERT INTO user_data(login, password, role) VALUES(?,?,?)",
                                     login, sha256(password.encode('utf-8')).hexdigest(),role)
            self._connection.commit()
        except Exception as ex:
            popup = Popup(title='Ошибка',content=TextInput(text=str(ex.args), size_hint=(None, None),size=(250, 250)))
            popup.open()

        finally:
            popup = Popup(title='Сообщение от БД', content=Button(text = r'Пользователь ' + login + 'успешно добавлен', size_hint=(None, None),
                                                                  size=(250, 250),on_click = popup.dismiss))
            popup.open()

