from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class LaborantScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        errorbutton = Button(
            text="Экран лаборанта",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.errorbutton_onclick,
        )
        gridlayout.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        gridlayout.add_widget(Button(text='Выход', on_press=self.BUTTON_exit, size_hint=(.5, 1)))
        gridlayout.add_widget(errorbutton)
        self.add_widget(gridlayout)

    def errorbutton_onclick(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'

    def BUTTON_exit(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'LOGIN_screen'