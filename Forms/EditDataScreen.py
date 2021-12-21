from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class EditDataScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        layout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        returnButton = Button(
        text="Назад",
        background_color=[2, 1.5, 3, 1],
        size_hint=[1, 0.1],
        on_press=self. BUTTON_return)

        label = Label(
            text="Экран редактирования информации В БД",
            line_height=4
        )

        gridlayout.add_widget(layout)
        gridlayout.add_widget(label)
        gridlayout.add_widget(returnButton)

        self.add_widget(gridlayout)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

