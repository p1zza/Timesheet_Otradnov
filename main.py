import re

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
    flag = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width = 200)
        login_label = Label(text="Введите Логин", font_size=20)
        self.login_value = TextInput(multiline=False, size_hint=(.5, .25),halign = 'center', font_size = 20, hint_text = 'Логин (4-20 символов)')
        password_label = Label(text="Введите Пароль", font_size=20)
        self.password_value = TextInput(multiline=False, size_hint=(.5, .25), password=True,halign = 'center',font_size = 20, hint_text = 'Пароль (8-20 символов)')

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
        nullabel18 = Label(text="", font_size=20)
        nullabel19 = Label(text="", font_size=20)
        nullabel20 = Label(text="", font_size=20)
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
        gridlayout.add_widget(nullabel8)
        gridlayout.add_widget(self.password_value)
        gridlayout.add_widget(nullabel9)
        gridlayout.add_widget(nullabel13)
        gridlayout.add_widget(Label(text='[color=ffffff][ref=]Посмотреть пароль [/ref][/color]', markup=True,
                                    on_ref_press=self.ShowPassword))

        gridlayout.add_widget(nullabel14)
        gridlayout.add_widget(nullabel15)
        gridlayout.add_widget(button_new_login)
        gridlayout.add_widget(nullabel16)
        gridlayout.add_widget(nullabel17)


        bottomlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10],size_hint=(1, .15))
        bottomlayout.add_widget(Button(text="Регистрация",size_hint=[1, .5],on_press=self.BUTTON_Message))

        Window.clearcolor = (0,0,0,0) #цвет бэкграунда
        self.add_widget(gridlayout)
        self.add_widget(bottomlayout)
        try:
            self.db = Database()
        except Exception as ex:
            popup = Popup(title='Ошибка',
                          content=TextInput(text=('\n\n\n'+str(ex.args)), multiline=True),
                          size_hint=(None, None), size=(200, 200),border = 'bottom')
            popup.open()

    def BUTTON_Message(self,*args):
        popup = Popup(title='Сообщение',content=TextInput(text='Данный функционал в разработке', multiline=True),size_hint=(None, None), size=(200, 200))
        popup.open()

    def ShowPassword(self, *args):
        if self.flag == 0:
            self.password_value.password =False
            self.flag+=1
        else:
            self.flag=0
            self.password_value.password =True

    def BUTTON_login(self, *args):
        try:
            auth_role = self.db.authenticate(self.login_value.text, self.password_value.text)
            if self.login_value.text == '':
                popup = Popup(title='Ошибка', content=TextInput(text='Поле ввода логина пустое', multiline=True), size_hint=(None, None),
                              size=(250, 250))
                popup.open()
            if self.password_value.text == '':
                popup = Popup(title='Ошибка', content=TextInput(text='Поле ввода пароля пустое', multiline=True),
                              size_hint=(None, None),
                              size=(250, 250))
                popup.open()

        except Exception as ex:
            popup = Popup(title='Ошибка', content=TextInput(text = ex.args,multiline=True), size_hint=(None, None), size=(250, 250))
            popup.open()

        finally:
            print (auth_role)
            if auth_role is None:
                popup = Popup(title='Ошибка',content=TextInput(text=str('Ошибка авторизации'),multiline=True),size_hint=(None, None), size=(250, 250))
                popup.open()
            elif auth_role == "admin":
                self.manager.transition.direction = 'left'
                self.manager.current = 'adminscreen'
            elif auth_role == "laborant":
                self.manager.transition.direction = 'left'
                self.manager.current = 'laborantscreen'

            self.login_value.text = ""
            self.password_value.text = ""



class PasswordingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='LOGIN_screen'))
        sm.add_widget(AdministratorScreen(name='adminscreen'))
        sm.add_widget(LaborantScreen(name='laborantscreen'))
        sm.add_widget(ImportScreen(name='IMPORT_screen'))
        sm.add_widget(UsersScreen(name='USERS_screen'))
        sm.add_widget(EditDataScreen(name='EditData_screen'))
        return sm

if __name__ == "__main__":
    PasswordingApp().run()
