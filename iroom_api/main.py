from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


class LoginScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class ClassScreen(Screen):
    pass


class InteractiveCScreen(Screen):
    def btn(self):
        show_popup_nonvideo()


class VideoCScreen(Screen):
    def btn(self):
        show_popup_video()

    
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

class video(FloatLayout):
    pass

class Nonvideo(FloatLayout):
    pass

def show_popup_nonvideo():
    show = Nonvideo()
    popupWindow= Popup(title="Popup Window", content= show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()

def show_popup_video():
    show = Video()
    popupWindow= Popup(title="Popup Window", content= show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()


class MyMainApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm


if __name__ == "__main__":
    MyMainApp().run()
