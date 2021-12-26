from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class EditDataScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        bottomlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10],size_hint=(1, .15))

        returnButton = Button(
        text="Назад",size_hint=(.5, .1),on_press=self. BUTTON_return,background_color=[0, 1.5, 3, 1])
        gridlayout.add_widget(Label(text="Редактирование данных",line_height=4))

        gridlayout.add_widget(Button(text="Редактирование списка дисциплин", size_hint=[1, .5], on_press = self.BUTTON_Message))
        gridlayout.add_widget(Button(text="Редактирование списка групп", size_hint=[1, .5], on_press = self.BUTTON_Message))
        gridlayout.add_widget(Button(text="Редактирование расписания звонков", size_hint=[1, .5], on_press = self.BUTTON_Message))
        gridlayout.add_widget(Button(text="Редактирование праздничных дней", size_hint=[1, .5], on_press = self.BUTTON_Message))
        gridlayout.add_widget(Button(text="Редактирование расписания", size_hint=[1, .5], on_press = self.BUTTON_Message))
        gridlayout.add_widget(Button(text="Редактирование списка аудиторий", size_hint=[1, .5], on_press = self.BUTTON_Message))

        bottomlayout.add_widget(returnButton)
        self.add_widget(gridlayout)
        self.add_widget(bottomlayout)

    def BUTTON_Message(self,*args):
        popup = Popup(title='Сообщение',content=TextInput(text=('Данный функционал в разработке'), multiline=True),size_hint=(None, None), size=(200, 200), border='bottom')
        popup.open()
    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

