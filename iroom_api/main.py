from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ClassScreen(Screen):
    pass


class InteractiveCScreen(Screen):
    pass


class VideoCScreen(Screen):
    pass

    
class ClassroomScreen(Screen):
    pass


class OfficeHoursScreen(Screen):
    pass


class MeetingReqScreen(Screen):
    pass


class ScheduleMeetingScreen(Screen):
    pass


class SendMessScreen(Screen):
    pass


class ViewMessScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm


if __name__ == "__main__":
    MyMainApp().run()
