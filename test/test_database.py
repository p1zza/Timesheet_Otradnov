import unittest
import os
from sqlite import Database


class DatabaseTestCase(unittest.TestCase):

    def setUp(self):
        # Тестовая БД лежит в директории test. Если понадобится использовать БД в той же директории что и при нормальной
        # работе, необходимо это:
        # if os.path.exists(os.path.join("..", "timesheet.db.bak")):
        #    os.remove(os.path.join("..", "timesheet.db.bak"))
        # if os.path.exists(os.path.join("..", "timesheet.db")):
        #    os.rename(os.path.join("..", "timesheet.db"), os.path.join("..", "timesheet.db.bak"))
        if os.path.exists("timesheet.db"):
            os.remove("timesheet.db")
        self.db = Database()
        with open("test_data.sql", 'r', encoding='utf-8') as file:
            sql_as_string = file.read()
        self.db.main_cursor.executescript(sql_as_string)

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
