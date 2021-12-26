from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput


class UsersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width=200)

        self.userNameValue = TextInput(multiline=False, size_hint=(1, .5),hint_text='Логин (4-20 символов)',halign = 'center', font_size = 20)
        self.PasswordValue = TextInput(multiline=False, size_hint=(1, .5),hint_text='Пароль (8-20 символов)',halign = 'center', font_size = 20,password=True)
        self.SPasswordValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Повторно введите пароль', halign='center',font_size=20,password=True)
        self.SurnameValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Фамилия (30 символов)',halign='center', font_size=20)
        self.patronymicValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Отчество (30 символов)',halign='center', font_size=20)
        self.nameValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Имя (30 символов)', halign='center',font_size=20)
        self.roleValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Роль', halign='center', font_size=20)
        self.mailValue = TextInput(multiline=False, size_hint=(1, .5), hint_text='Почта в домене @mirea.ru', halign='center', font_size=20)
        layout.add_widget(Label(text="Введите логин пользователя",line_height=1))
        layout.add_widget(Label(text="Введите Фамилию",line_height=1))
        layout.add_widget(Label(text="Введите Отчество",line_height=1))
        layout.add_widget(self.userNameValue)
        layout.add_widget(self.SurnameValue)
        layout.add_widget(self.patronymicValue)
        layout.add_widget(Label(text="Придумайте пароль",line_height=1))
        layout.add_widget(Label(text="Введите полное Имя"))
        layout.add_widget(Label(text="Введите роль"))
        layout.add_widget(self.PasswordValue)
        layout.add_widget( self.nameValue)
        layout.add_widget(self.roleValue)
        layout.add_widget(self.SPasswordValue)
        layout.add_widget(self.mailValue)
        layout.add_widget(Button(text="Добавить Пользователя", size_hint=[1, 0.1], on_press=self.BUTTON_AddUser,background_color=[0, 1.5, 3, 1]))
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))

        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        layout.add_widget(Button(text="Назад",size_hint=[1, 0.1],on_press=self. BUTTON_return,background_color=[0, 1.5, 3, 1]))
        self.add_widget(layout)

        bottommenu = BoxLayout(orientation='horizontal', size_hint=(1, .15))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget((Button(text='', disabled=True, size_hint=(.5, 1))))
        bottommenu.add_widget(TextInput(multiline=True,text = "список пользователей в БД:"))
        self.add_widget(bottommenu)

        #TODO: У полей следующее поведение: стоит некоторое ограничение по количеству символов.
        # Они отсекаются в момент нажатия на кнопку «Добавить пользователя»
        # и об этом сообщается пользователь.
        # Подсказка серым текстом Логин(диапазон символов 4-20), пароль *(8-20),
        # остальные поля по 30 символов. Выпадающий список роли
        # Обязательные поля - Фамилия, Имя, Доступ (по умолчанию - юзер), лог и пароль
        # В случае когда мы заполнили поля и тыкнули назад -данные не чистятся, две инпута с паролем.
        # При нажатии кнопки назад второе поле пароля очищается
        # При каждом незаполненном обязательном поле нужно проверить, что появляется ошибка -> кейсы
        # поле почты обязательное - либо @mirea.ru и @edu.mirea.ru - На будущее поменять
        # не заполнено несколько обязательбных полей -> добавить -> перечисление какие не заполнены
        # TODO:блокируем добавление пользователя через UI. ПО кнопке "дОбавить пользователя"
        # Функционал в разработке


    def BUTTON_AddUser(self,*args):
        popup = Popup(title='Сообщение',content=TextInput(text=('Данный функционал в разработке'), multiline=True),size_hint=(None, None), size=(200, 200), border='bottom')
        popup.open()

    def BUTTON_return(self, *args):
        self.SPasswordValue.text = ""
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

