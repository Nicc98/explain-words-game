from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp

class RoundResultsScreen(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.ids.header_label.text = f"{self.app.game_manager.round_number}. kārtas rezultāti"
        self.populate_round_results_list()

    def on_leave(self, *args):
        self.ids.round_results_list.clear_widgets()

    def continue_game(self):
        self.app.game_manager.after_round_results_screen()

    def populate_round_results_list(self):
        round_number = self.app.game_manager.round_number
        for team in self.app.game_manager.all_teams.values():
            turn_score = OneLineIconListItem(
                text = f"{team.name}: {team.get_turn_score(round_number)}",
                text_color = "#ffffff"
            )
            self.ids.round_results_list.add_widget(turn_score)

        