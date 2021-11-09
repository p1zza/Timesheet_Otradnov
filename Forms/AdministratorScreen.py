from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class AdministratorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        uppermenu = BoxLayout(orientation="horizontal", spacing=5, padding=[10])
        button_upper = Button(
            text="Верхняя кнопка",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.BUTTON_return,
        )

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

        uppermenu.add_widget(button_upper)
        self.add_widget(uppermenu)

        mainmenu.add_widget(button_new_pasword1)
        self.add_widget(mainmenu)

        bottomMenu.add_widget(button_new_pasword2)
        bottomMenu.add_widget(button_new_pasword3)
        self.add_widget(bottomMenu)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'