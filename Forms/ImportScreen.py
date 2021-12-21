from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import tkinter.filedialog

import data_imports
import sqlite


class ImportScreen(Screen):
    label=Label()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        returnButton = Button(
            text="Переход в меню",
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return
        )
        importButton = Button(
            text="Импорт расписания",
            size_hint=[1, 0.1],
            on_press=self.BUTTON_import
        )
        importRoomsButton = Button(
            text="Импорт аудиторий",
            size_hint=[1, 0.1],
            on_press=self.BUTTON_importRooms
        )
        clearButton = Button(
            text="Очистить путь",
            size_hint=[1, 0.1],disabled=True)

        self.label = Label(text = "Расписание еще не загружено, Вы можете стать первым!",line_height = 4)
        layout.add_widget(importButton)
        layout.add_widget(importRoomsButton)
        layout.add_widget(clearButton)
        layout.add_widget(self.label)
        layout.add_widget(returnButton)

        self.add_widget(layout)

        self.db = sqlite.Database()  # Обращение к Singleton

    def BUTTON_importRooms(self, *args):
        filepath = tkinter.filedialog.askopenfilename(title="Выберите файл с аудиториями",
                                                      filetypes=(('csv files', '*.csv'),))
        rooms, types = data_imports.import_rooms_from_file(filepath)

        for room_type in types:
            try:
                self.db.add_room_type(room_type)
            except sqlite.AlreadyExistsError:
                print("RoomType to DB - AlreadyExists")
                pass
        for room in rooms:
            try:
                self.db.add_room(room)
            except sqlite.AlreadyExistsError:
                print("Room to DB - AlreadyExists")
                pass

    def BUTTON_import(self, *args):

        filepath = tkinter.filedialog.askopenfilename(title="Выберите файл с расписанием",filetypes=(('xls files','*.xls'),))


        #TODO: должна иметься информация о файле – либо файл такой же, как и был до загрузки нового файла, либо дату последней загрузки файла.
        #TODO: если не выбрали файл, строка ниже не отображается. Отображается исходное сообщение
        #TODO: кнопка отмены/сброса расписания
        #TODO: строка информации о файле с датами. ЕЩЁ не загружена таблица (в данный момент никаких данных нет)
        #TODO: так как мы рассматриваем данный фу
        self.label.text = "Выбран путь: \n " + filepath
        #TODO:Отображение модального окна - СОхранить и отменить. Кнопка Отмены вернет нас в основное окно с надписиью "Вы первый"
        # или "путь до файла"
        #TODO:Если так нельзя сделать, делаем отбойник через дизаблед кнопку "Сохранить" рядом с кнопкой "Очистить путь".
        # Обе кнопки на момент открытия рабочего места должны быть заблокированы. В случае выбора или корректной валидации
        # обе кнопки активируются.
        #TODO: Выбираем файл -> активируются кнопки ->  выходим с формы -> модальное окно "Вы пытаетесь выйти без сохранения"


        #TODO: тут пересылка на обработку файла с расписанием. ниже пример
        #TODO: дать кнопку дополнительного подтверждения выгрузки файла после импорта


        #TODO: файл не соответствует шаблону, слишком маленький размер файла

        '''
    def import_nodes(self):
        filepath = filedialog.askopenfilenames(filetypes = (('xls files','*.xls'),))
        if not filepath:
            return
        else:
            filepath ,= filepath
        book = xlrd.open_workbook(filepath)
        try:
            sheet = book.sheet_by_index(0)
        # if the sheet cannot be found, there's nothing to import
        except xlrd.biffh.XLRDError:
            warnings.warn('the excel file is empty: import failed')
        for row_index in range(1, sheet.nrows):
            x, y = self.to_canvas_coordinates(*sheet.row_values(row_index))
            self.create_object(x, y) 
                       
        '''

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'