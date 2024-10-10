from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.screens import HomeScreen, SettingsScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyApp().run()
