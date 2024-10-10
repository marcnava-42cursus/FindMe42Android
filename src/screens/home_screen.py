from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Pantalla Principal'))
        self.add_widget(Button(text='Ir a Configuración', on_press=self.go_to_settings))

    def go_to_settings(self, instance):
        self.manager.current = 'settings'
