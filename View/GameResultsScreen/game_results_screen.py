from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class GameResultsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def continue_game(self):
        self.app.game_manager.after_game_results_screen()