from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
