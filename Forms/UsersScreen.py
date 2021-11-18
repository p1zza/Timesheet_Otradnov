from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


class UsersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        layout = BoxLayout(orientation="vertical", spacing=5, padding=[10])
        returnButton = Button(
        text="Назад",
        background_color=[2, 1.5, 3, 1],
        size_hint=[1, 0.1],
        on_press=self. BUTTON_return)

        label = Label(
            text="Экран редактирования списка пользователей",
            line_height=4
        )

        boxlayout.add_widget(layout)
        boxlayout.add_widget(label)
        boxlayout.add_widget(returnButton)



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
        self.add_widget(boxlayout)

    def BUTTON_return(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'adminscreen'

