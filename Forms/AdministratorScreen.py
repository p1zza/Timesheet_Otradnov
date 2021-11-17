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
        layout.add_widget(Button(text='Редактирование'))
        layout.add_widget(Button(text='Уведомления'))
        layout.add_widget(Button(text='Пользователи'))
        layout.add_widget(Button(text='Расписание дежурств'))
        layout.add_widget(Button(text='Изменение расписания'))
        layout.add_widget(Button(text='Перенести пару'))
        layout.add_widget(Button(text='Заменить преподавателя'))
        layout.add_widget(Button(text='Статус',on_press = self.BUTTON_status))
        layout.add_widget(Button(text='Назад'))

        mainmenu = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        button_new_pasword1 = Button(
            text="Return",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return,
        )

        bottomMenu = BoxLayout(orientation="horizontal", spacing=5, padding=[10])
        button_new_pasword2 = Button(
            text="button horizontal",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return,
        )
        button_new_pasword3 = Button(
            text="button horizontal",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return,
        )

        bottomMenu.add_widget(button_new_pasword2)
        bottomMenu.add_widget(button_new_pasword3)
        self.add_widget(layout)
        self.add_widget(bottomMenu)

    def BUTTON_ImportTimesheet(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'IMPORT_screen'

    def BUTTON_status (self, *args):
        #TODO: получение информации о статусе данных в БД
        self.butt = Button(text="Для закрытия окна нажмите в любое место",on_press=self.BUTTON_removeStatus)
        self.add_widget(self.butt)

    def BUTTON_removeStatus(self,*args):
        self.remove_widget(self.butt)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'