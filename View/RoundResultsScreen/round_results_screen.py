from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp

class RoundResultsScreen(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()

    def continue_game(self):
        a = 1

    def populate_results_screen(self):
        a = 1
        # team = OneLineIconListItem(
        #     text = f"Team '{self.current_team_name}' score: {self.game_manager.get_team_round_score(self.current_team_name, self.current_round_number)}",
        #     # icon = "crown"
        #     # icon = "emoticon-poop"
        # )
        # self.ids.team_list.add_widget(new_team)
        # pos_hint_y = 0.5


        