from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Forms.LaborantScreen import LaborantScreen
from Forms.AdministratorScreen import AdministratorScreen
from Forms.ImportScreen import ImportScreen
from Forms.UsersScreen import UsersScreen

class ScreenMain(Screen):
    login = ""
    password = ""
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        login_label = Label(text = "Введите Логин", font_size = 20)
        self.login_value = TextInput(multiline= False, size_hint= (1,.5))
        password_label = Label(text="Введите Пароль", font_size=20)
        self.password_value = TextInput(multiline=False, size_hint=(1, .5), password=True)

        button_new_pasword = Button(
            text="Вход",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, .5],
            on_press=self.BUTTON_login
        )

        boxlayout.add_widget(login_label)
        boxlayout.add_widget(self.login_value)
        boxlayout.add_widget(password_label)
        boxlayout.add_widget(self.password_value)
        boxlayout.add_widget(button_new_pasword)

        self.add_widget(boxlayout)

    def BUTTON_login(self, *args):
#TODO тут проверка роли пользователя
        self.login = self.login_value.text
        self.password = self.password_value.text
        print(self.login, self.password)

        if self.login == "administrator":
            self.manager.transition.direction = 'left'
            self.manager.current = 'adminscreen'
        elif self.login == "laborant":
            self.manager.transition.direction = 'left'
            self.manager.current = 'laborantscreen'
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = 'errorscreen'

class ErrorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        errorbutton = Button(
            text="Ошибка. Нажмите для возврата на главный экран",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self.errorbutton_onclick,
        )
        boxlayout.add_widget(errorbutton)
        self.add_widget(boxlayout)

    def errorbutton_onclick(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'LOGIN_screen'

class PaswordingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='LOGIN_screen'))
        sm.add_widget(AdministratorScreen(name='adminscreen'))
        sm.add_widget(ErrorScreen(name='errorscreen'))
        sm.add_widget(LaborantScreen(name='laborantscreen'))
        sm.add_widget(ImportScreen(name='IMPORT_screen'))
        sm.add_widget(UsersScreen(name='USERS_screen'))
        return sm

if __name__ == "__main__":
    PaswordingApp().run()