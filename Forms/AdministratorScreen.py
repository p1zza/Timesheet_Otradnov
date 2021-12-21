from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



class AdministratorScreen(Screen):
    layout = GridLayout()
    butt = Button()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=5, row_force_default=True, row_default_height=40)
        layout.add_widget(Button(text='Импорт расписания',on_press=self.BUTTON_ImportTimesheet))
        layout.add_widget(Button(text='Редактирование',on_press=self.BUTTON_EditData))
        layout.add_widget(Button(text='Уведомления', disabled = True))
        layout.add_widget(Button(text='Пользователи',on_press = self.BUTTON_users))
        layout.add_widget(Button(text='Расписание дежурств', disabled = True))
        layout.add_widget(Button(text='Статус', on_press=self.BUTTON_status))
        layout.add_widget(Button(text='Изменение расписания'))
        layout.add_widget(Button(text='Перенести пару', disabled = True))
        layout.add_widget(Button(text='Заменить преподавателя', disabled = True))
        layout.add_widget(Button(text='Назад',on_press = self.BUTTON_return))

        bottommenu = BoxLayout(orientation = 'horizontal',size_hint=(1, .15))
        bottommenu.add_widget((Button(text='', disabled = True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget(Button(text='Выход',on_press=self.BUTTON_exit, size_hint=(.5, 1)))


        self.add_widget(layout)
        self.add_widget(bottommenu)


    def BUTTON_users(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'USERS_screen'

    def BUTTON_exit(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'LOGIN_screen'

    def BUTTON_ImportTimesheet(self,*args):
        # TODO: обработка ексель-файла
        self.manager.transition.direction = 'left'
        self.manager.current = 'IMPORT_screen'

    def BUTTON_status (self, *args):
        #TODO: получение информации о статусе данных в БД
        self.butt = Button(text="Для закрытия окна нажмите в любое место",on_press=self.BUTTON_removeStatus)
        self.add_widget(self.butt)

    def BUTTON_removeStatus(self,*args):
        self.remove_widget(self.butt)

    def BUTTON_EditData(self,*args):
        # TODO: изменение данных в бд. Форма редактирования
        self.manager.transition.direction = 'left'
        self.manager.current = 'EditData_screen'

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'