-- Admin and laborant already created
INSERT INTO user_data(login, password, role)
 VALUES('laborant2',
        'b3d3bcad6ad0cb28e25e68f80f37a85d092fed3a9f0c2309c268de943f3a4b95', -- pass: laborant
        'laborant');

INSERT INTO room_types (type)
 VALUES ('lection');
INSERT INTO room_types (type)
 VALUES ('computer');
INSERT INTO room_types (type)
 VALUES ('practice');

INSERT INTO rooms (type_id, campus, number)
 VALUES (
         1,
         'Стромынка',
         '381'
        );
INSERT INTO rooms (type_id, campus, number)
 VALUES (
         2,
         'Стромынка',
         'КБ-1 13'
        );
INSERT INTO rooms (type_id, campus, number)
 VALUES (
         1,
         'В-78',
         'A11'
        );

INSERT INTO personal_data (name, surname, patronymic, email, phone, photo)
 VALUES (
         'Иван',
         'Иванов',
         'Иванович',
         'example@mail.ru',
         '+79151150105',
         NULL
        );
INSERT INTO personal_data (name, surname, patronymic, email, phone, photo)
 VALUES (
         'Александр',
         'Тимофеев',
         'Евгеньевич',
         'saloed@gmail.com',
         '+79870778323',
         NULL
        );
INSERT INTO personal_data (name, surname, patronymic, email, phone, photo)
 VALUES (
         'Валерия',
         'Головченко',
         'Игоревна',
         'helpme@yandex.ru',
         '+79777777777',
         NULL
        );

INSERT INTO lecturers (personal_id)
 VALUES (1);
INSERT INTO lecturers (personal_id)
 VALUES (2);
INSERT INTO lecturers (personal_id)
 VALUES (3);

INSERT INTO groups (name)
 VALUES ('БАСО-01-17');
INSERT INTO groups (name)
 VALUES ('БАСО-02-17');
INSERT INTO groups (name)
 VALUES ('БАСО-03-17');
INSERT INTO groups (name)
 VALUES ('БАСО-04-17');

INSERT INTO subjects (name)
 VALUES ('Физика');
INSERT INTO subjects (name)
 VALUES ('Организационное и правовое обеспечение информационной безопасности');
INSERT INTO subjects (name)
 VALUES ('Технические средства защиты объектов');

INSERT INTO class_types (name)
 VALUES ('Лекционно');
INSERT INTO class_types (name)
 VALUES ('Практическое');
INSERT INTO class_types (name)
 VALUES ('Лабораторное');

INSERT INTO teach_plan (group_id, subject_id, class_type_id, hours)
 VALUES (
         1,
         3,
         2,
         40
        );
INSERT INTO teach_plan (group_id, subject_id, class_type_id, hours)
 VALUES (
         1,
         3,
         1,
         60
        );
INSERT INTO teach_plan (group_id, subject_id, class_type_id, hours)
 VALUES (
         3,
         1,
         3,
         20
        );

INSERT INTO timesheet (room_id, lecturer_id, group_id, class_type_id, subject_id, date, class_number)
 VALUES (
         2,
         3,
         1,
         2,
         2,
         '10.09.2021',
         4
        );
INSERT INTO timesheet (room_id, lecturer_id, group_id, class_type_id, subject_id, date, class_number)
 VALUES (
         2,
         2,
         3,
         2,
         3,
         '10.09.2021',
         5
        );
INSERT INTO timesheet (room_id, lecturer_id, group_id, class_type_id, subject_id, date, class_number)
 VALUES (
         3,
         1,
         4,
         1,
         1,
         '14.09.2021',
         1
        );