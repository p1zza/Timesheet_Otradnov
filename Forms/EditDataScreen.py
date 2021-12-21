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
        bottomlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10],size_hint=(1, .15))

        returnButton = Button(
        text="Назад",size_hint=(.5, .1),on_press=self. BUTTON_return)
        gridlayout.add_widget(Label(
            text="Экран редактирования информации В БД",
            line_height=4
        ))

        #TODO: сверху экрана надпись с кнопки
        gridlayout.add_widget(Button(text="Редактирование списка дисциплин", size_hint=[1, .5], disabled=True))
        gridlayout.add_widget(Button(text="Редактирование списка групп", size_hint=[1, .5], disabled=True))
        gridlayout.add_widget(Button(text="Редактирование расписания звонков", size_hint=[1, .5], disabled=True))
        gridlayout.add_widget(Button(text="Редактирование праздничных дней", size_hint=[1, .5], disabled=True))
        gridlayout.add_widget(Button(text="Редактирование расписания", size_hint=[1, .5], disabled=True))
        gridlayout.add_widget(Button(text="Редактирование списка аудиторий", size_hint=[1, .5], disabled=True))

        bottomlayout.add_widget(returnButton)
        self.add_widget(gridlayout)
        self.add_widget(bottomlayout)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

