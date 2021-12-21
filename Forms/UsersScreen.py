from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput

from sqlite import Database as DB

class UsersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=3, row_force_default=True, row_default_height=40, col_default_width=200)

        self.userNameValue = TextInput(multiline=False, size_hint=(1, .5))
        self.PasswordValue = TextInput(multiline=False, size_hint=(1, .5))

        layout.add_widget(Label(text="Введите имя пользователя",line_height=1))
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        layout.add_widget(self.userNameValue)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text="Придумайте пароль",line_height=1))
        #TODO: hint_text='Пароль'
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        layout.add_widget(self.PasswordValue)
        layout.add_widget(Label(text=""))
        layout.add_widget(Button(text="Назад",size_hint=[1, 0.1],on_press=self. BUTTON_return))
        layout.add_widget(Label(text=""))
        layout.add_widget(Button(text="Добавить Пользователя",size_hint=[1, 0.1],on_press = self.BUTTON_AddUser))
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


        '''
        dropdown = DropDown()
        for index in range(10):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        mainbutton = Button(text='Hello', size_hint=(None, None))

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        mainbutton.bind(on_release=dropdown.open)

        # one last thing, listen for the selection in the dropdown list and
        # assign the data to the button text.
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        runTouchApp(mainbutton)
        boxlayout.add_widget(dropdown)
        '''

    def BUTTON_AddUser(self,*args):
        role = 'admin'
        DB.add_user(self,self.userNameValue.text, self.PasswordValue.text, role)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

