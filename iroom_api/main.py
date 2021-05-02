from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# Builder.load_file('widgets.kv')

#Layout for the Login Screen on the Application
class LoginScreen(GridLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def btn(self):
        print("Welcome", self.username.text)
    pass


class Background(Widget):
    pass


class HomeScreen(Widget):
    pass


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    MyApp().run()
