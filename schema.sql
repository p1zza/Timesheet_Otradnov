CREATE TABLE IF NOT EXISTS user_data (
    uid NUMERIC PRIMARY KEY ASC,
    login TEXT UNIQUE,
    password TEXT,
    role TEXT
);

CREATE TABLE IF NOT EXISTS room_types (
    id NUMERIC PRIMARY KEY ASC,
    type TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS rooms (
    id NUMERIC PRIMARY KEY ASC,
    type_id NUMERIC,
    campus TEXT,
    number NUMERIC,
    FOREIGN KEY(type_id) REFERENCES room_types(id)
);

CREATE TABLE IF NOT EXISTS personal_data (
    id NUMERIC PRIMARY KEY ASC,
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    email TEXT,
    phone TEXT,
    photo BLOB
);

CREATE TABLE IF NOT EXISTS lecturers (
    personal_id NUMERIC,
    FOREIGN KEY(personal_id) REFERENCES personal_data(id)
);

CREATE TABLE IF NOT EXISTS groups (
    id NUMERIC PRIMARY KEY ASC,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS subjects (
    id NUMERIC PRIMARY KEY ASC,
    name TEXT
);
CREATE TABLE IF NOT EXISTS class_types (
    id NUMERIC PRIMARY KEY ASC,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS teach_plan (
    id NUMERIC PRIMARY KEY ASC,
    group_id NUMERIC,
    subject_id NUMERIC,
    class_type_id NUMERIC,
    hours NUMERIC,
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (class_type_id) REFERENCES class_types(id)
);

CREATE TABLE IF NOT EXISTS timesheet (
    id NUMERIC PRIMARY KEY ASC,
    room_id NUMERIC,
    lecturer_id NUMERIC,
    group_id NUMERIC,
    class_type_id NUMERIC,
    subject_id NUMERIC,
    date DATE,
    class_number NUMERIC,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    FOREIGN KEY (lecturer_id) REFERENCES lecturers(personal_id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (class_type_id) REFERENCES class_types(id)
);

CREATE TABLE IF NOT EXISTS timesheet_saves (
    id NUMERIC PRIMARY KEY ASC,
    timestamp INTEGER,
    hash TEXT,
    saved_uid INTEGER,
    FOREIGN KEY (saved_uid) REFERENCES user_data(uid)
);