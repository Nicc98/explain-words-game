from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp

class GameResultsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.populate_game_results_list()

    def on_leave(self, *args):
        self.ids.game_results_list.clear_widgets()

    def continue_game(self):
        self.app.game_manager.after_game_results_screen()

    def populate_game_results_list(self):
        for team in self.app.game_manager.all_teams.values():
            turn_score = OneLineIconListItem(
                text = f"{team.name}: {team.total_score}",
                text_color = "#ffffff"
            )
            self.ids.game_results_list.add_widget(turn_score)