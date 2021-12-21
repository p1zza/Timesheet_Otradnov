import csv
import data_models


def import_rooms_from_file(path):
    rooms = []
    types = {}
    with open(path, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] not in types:
                types[row[0]] = data_models.RoomType(row[0])
            rooms.append(data_models.Room(row[1], row[2], types[row[0]]))
    return rooms, types.values()
