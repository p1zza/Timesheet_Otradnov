from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class LaborantScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        errorbutton = Button(
            text="Экран лаборанта",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.errorbutton_onclick,
        )

        boxlayout.add_widget(errorbutton)
        self.add_widget(boxlayout)

    def errorbutton_onclick(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'