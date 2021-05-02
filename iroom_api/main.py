from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# Builder.load_file('widgets.kv')

#Layout for the Login Screen on the Application
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="iRoom"))
        self.inside.add_widget(Label(text="help"))

        self.inside.add_widget(Label(text="User Name: "))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="Password: "))
        self.password = TextInput(password=True, multiline=False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)

        self.login = Button(text="Log In", font_size=30)
        self.login.bind(on_press=self.pressed)
        self.add_widget(self.login)

    def pressed(self, instance):
        userName = self.username.text
        print("Welcome", userName)


class Background(Widget):
    pass


class HomeScreen(Widget):
    pass


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    MyApp().run()
