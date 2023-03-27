from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

class TeamCreationScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def go_to_game(self):
        if len(list(self.ids.team_list.children)) > 0:
            self.app.game_manager.after_team_creation_screen()
        else:
            print("Not enough teams added!")
        # TODO add error message saying that at least 1 team needs to be added

    def add_team(self):
        team_name = self.ids.team_name_input.text
        if not team_name:
            return
        # TODO maybe add custom list item to preset color, font, etc.
        new_team = OneLineIconListItem(
            text = team_name,
            text_color = "#ffffff"
        )
        self.ids.team_list.add_widget(new_team)
        self.ids.team_name_input.text = ''
        self.app.game_manager.add_team(team_name)
        


