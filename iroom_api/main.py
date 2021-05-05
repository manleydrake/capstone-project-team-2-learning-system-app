from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv = Builder.load_file("my.kv")


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass

class ClassScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm


if __name__ == "__main__":
    MyMainApp().run()

# Layout for the Login Screen on the Application
# class LoginScreen(GridLayout):


#    def btn(self):
#        print("Welcome", self.username.text)
#   pass

# class Background(Widget):
#    pass


# class HomeScreen(Widget):

#   pass


# sm = ScreenManager()
# sm.add_widget(LoginScreen(name='loginscreen'))
# sm.add_widget(HomeScreen(name='homescreen'))
# return sm
# return LoginScreen()
