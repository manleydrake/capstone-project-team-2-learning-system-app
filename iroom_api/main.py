from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

# Builder.load_file('widgets.kv')


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="iRoom"))
        self.add_widget(Label(text="help"))
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text="Log in"))


class Background(Widget):
    pass


class HomeScreen(Widget):
    pass


class MyApp(App):
    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    MyApp().run()
