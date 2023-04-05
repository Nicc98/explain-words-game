from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

from View.common.components.widget_templates import ScoreListItem

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
        for team in self.app.game_manager.get_sorted_teams():
            turn_score = ScoreListItem(
                text = team[0],
                icon = team[1],
                score = team[2]
            )
            self.ids.game_results_list.add_widget(turn_score)