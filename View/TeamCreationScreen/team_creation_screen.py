from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

class TeamCreationScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.all_teams = []

    def go_to_game(self):
        if len(list(self.ids.team_list.children)) > 0:
            self.app.root.set_current_screen("Game")
            self.store_teams()
        # TODO add error message saying that at least 1 team needs to be added

    def add_team(self):
        team_name = self.ids.team_name_input.text
        if not team_name:
            return
        # TODO maybe add custom list item to preset color, font, etc.
        new_team = OneLineIconListItem(
            text = team_name
        )
        self.ids.team_list.add_widget(new_team)
        self.ids.team_name_input.text = ''
        team_info = {
            'name': team_name,
            'total_score': 0,
            'round_scores': {}
        }
        self.all_teams.append(team_info)
    
    def store_teams(self):
        self.app.storage_manager.set_value('teams', self.all_teams)
        print(f"All Teams: {self.app.storage_manager.get('teams')}")


