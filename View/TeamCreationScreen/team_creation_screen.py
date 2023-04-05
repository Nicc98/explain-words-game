import random

from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.toast import toast

from View.common.components.widget_templates import TeamListItem

class TeamCreationScreen(MDScreen):

    # TODO Maybe add hard mode toggle and time changer in this screen
    # or add a new screen for that after this screen

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def go_to_game(self):
        if len(list(self.ids.team_list.children)) > 0:
            self.app.game_manager.after_team_creation_screen()
        else:
            toast('Jāpievieno vismaz 1 komanda!')

    def add_team(self):
        team_name = self.ids.team_name_input.text
        if not team_name:
            return
        random_icon = random.choice(self.app.icons)
        new_team = TeamListItem(text = team_name, icon = random_icon)
        self.ids.team_list.add_widget(new_team)
        self.ids.team_name_input.text = ''
        self.app.game_manager.add_team(team_name, random_icon)
