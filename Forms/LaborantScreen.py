from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class LaborantScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        LaboratnLabel = Label(text="Экран лаборанта",size_hint=[1, 0.1])
        gridlayout.add_widget(LaboratnLabel)
        gridlayout.add_widget((Button(text='Заявка на изменение расписания', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='Перенести пару', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='Заменить преподавателя', disabled=True, size_hint=(.5, 1))))

        self.add_widget(gridlayout)

        bottommenu = BoxLayout(orientation = 'horizontal',size_hint=(1, .15))
        bottommenu.add_widget((Button(text='', disabled = True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget(Button(text='Выход',on_press=self.BUTTON_exit, size_hint=(.5, 1)))
        self.add_widget(bottommenu)


    def BUTTON_exit(self,*args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'

    def errorbutton_onclick(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'

    def BUTTON_exit(self,*args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'