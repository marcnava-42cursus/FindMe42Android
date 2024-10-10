from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Pantalla de Configuración'))
        self.add_widget(Button(text='Volver', on_press=self.go_back))

    def go_back(self, instance):
        self.manager.current = 'home'
