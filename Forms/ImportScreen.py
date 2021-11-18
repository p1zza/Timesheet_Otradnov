from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import tkinter.filedialog


class ImportScreen(Screen):
    label=Label()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        returnButton = Button(
            text="Return",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return
        )
        importButton = Button(
            text="Импорт расписания",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_import
        )
        self.label = Label(
            text = "Тут информация о файле",
            line_height = 4
        )
        layout.add_widget(importButton)
        layout.add_widget(self.label)
        layout.add_widget(returnButton)

        self.add_widget(layout)

    def BUTTON_import(self, *args):
        filepath = tkinter.filedialog.askopenfilename(title="Выберите файл с расписанием",
                                                        filetypes=(('xls files','*.xls'),))

        self.label.text = "Выбран путь: \n " + filepath

        #TODO: тут пересылка на обработку файла с расписанием. ниже пример

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