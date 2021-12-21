from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Forms.LaborantScreen import LaborantScreen
from Forms.AdministratorScreen import AdministratorScreen
from Forms.ImportScreen import ImportScreen
from Forms.UsersScreen import UsersScreen
from Forms.EditDataScreen import EditDataScreen
from kivy.core.window import Window

from sqlite import Database


class ScreenMain(Screen):
    login = ""
    password = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.db = Database()  # TODO: Поймать sqlite3.Error и обработать

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        login_label = Label(text="Введите Логин", font_size=20)
        self.login_value = TextInput(multiline=False, size_hint=(.5, .25),halign = 'center', font_size = 20)
        password_label = Label(text="Введите Пароль", font_size=20)
        self.password_value = TextInput(multiline=False, size_hint=(.5, .25), password=True,halign = 'center',font_size = 20)

        nullabel1 = Label(text="", font_size=20)
        nullabel2 = Label(text="", font_size=20)
        nullabel3 = Label(text="", font_size=20)
        nullabel4 = Label(text="", font_size=20)
        nullabel5 = Label(text="", font_size=20)
        nullabel6 = Label(text="", font_size=20)
        nullabel7 = Label(text="", font_size=20)
        nullabel8 = Label(text="", font_size=20)
        nullabel9 = Label(text="", font_size=20)
        nullabel10 = Label(text="", font_size=20)
        nullabel11 = Label(text="", font_size=20)
        nullabel12 = Label(text="", font_size=20)
        nullabel13 = Label(text="", font_size=20)
        nullabel14 = Label(text="", font_size=20)
        nullabel15 = Label(text="", font_size=20)
        nullabel16 = Label(text="", font_size=20)
        nullabel17 = Label(text="", font_size=20)
        button_new_login = Button(
            text="Вход",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, .5],
            on_press=self.BUTTON_login
        )
        gridlayout.add_widget(nullabel10)
        gridlayout.add_widget(nullabel11)
        gridlayout.add_widget(nullabel12)
        gridlayout.add_widget(nullabel1)
        gridlayout.add_widget(login_label)
        gridlayout.add_widget(nullabel2)
        gridlayout.add_widget(nullabel3)
        gridlayout.add_widget(self.login_value)
        gridlayout.add_widget(nullabel4)
        gridlayout.add_widget(nullabel5)
        gridlayout.add_widget(password_label)
        gridlayout.add_widget(nullabel6)
        gridlayout.add_widget(Label(text = 'Минимально 8 символов'))
        gridlayout.add_widget(self.password_value)
        gridlayout.add_widget(nullabel8)
        gridlayout.add_widget(nullabel9)
        gridlayout.add_widget(nullabel13)
        gridlayout.add_widget(nullabel14)
        gridlayout.add_widget(nullabel15)
        gridlayout.add_widget(button_new_login)
        gridlayout.add_widget(nullabel16)
        gridlayout.add_widget(nullabel17)
        gridlayout.add_widget(Button(text="Регистрация",size_hint=[1, .5],disabled=True))

        Window.clearcolor = (0,0,0,0) #цвет бэкграунда
        self.add_widget(gridlayout)

    def BUTTON_login(self, *args):
        auth_role = self.db.authenticate(self.login_value.text, self.password_value.text)
        print (auth_role)
        if auth_role is None:
            popup = Popup(title='Ошибка',content=TextInput(text=str(
                '==Ошибка авторизации.== \n Пользователь с именем: <' + str(self.login_value.text)+'> и ролью <'+str(auth_role)+'> не найден в БД. \n'+
            '\n ==Нажмите в любом месте для продолжения работы=='),
                multiline=True),size_hint=(None, None), size=(250, 250))
            popup.open()
            #self.manager.transition.direction = 'right'
            #self.manager.current = 'errorscreen'
        elif auth_role == "admin":
            self.manager.transition.direction = 'left'
            self.manager.current = 'adminscreen'
        elif auth_role == "laborant":
            self.manager.transition.direction = 'left'
            self.manager.current = 'laborantscreen'

        self.login_value.text = ""
        self.password_value.text = ""


class ErrorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        errorbutton = Button(
            text="Ошибка. Нажмите для возврата на главный экран",
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
        sm.add_widget(EditDataScreen(name='EditData_screen'))
        return sm


if __name__ == "__main__":
    PaswordingApp().run()
