from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem

class TeamCreationScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_team(self):
        team_name = self.ids.team_name_input.text
        if not team_name:
            return
        # Todo maybe add custom list item to preset color, font, etc.
        new_team = OneLineIconListItem(
            text = team_name
        )
        self.ids.team_list.add_widget(new_team)
        self.ids.team_name_input.text = ''

