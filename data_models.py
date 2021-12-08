class PersonalData:
    def __init__(self, id, name, surname, patronymic, email, phone, photo=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.email = email
        self.phone = phone
        self.photo = photo


class RoomType:
    def __init__(self, id, type):
        self.id = id
        self.type = type


class Room:
    def __init__(self, id, campus, number, type):
        self.id = id
        self.campus = campus
        self.number = number
        self.type = type


class Duty:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end


class Lecturer:
    def __init__(self, id, personal_data, work_time, duty):
        self.id = id
        self.personal_data = personal_data
        self.work_time = work_time
        self.duty = duty


class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class EducationType:
    def __init__(self, id, name):
        self.id = id
        self.name = name


