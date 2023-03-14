from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock

import random

class GameScreen(MDScreen):

    # TODO Add hard mode toggle switch in settings:
    # If enabled then when a word is skipped, 5 (or other amount)
    # of seconds get removed from the timer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.words = [
            "Abols", "Kaposts", "Pica", "Saldejums",
            "Burgers", "Burrito", "Zupa", "Sacepums"
        ]
        self.max_words = 8
        self.words_pulled = 0
        self.current_team_index = 0
    
    def on_enter(self, *args) -> None:
        print(f"All Teams: {self.app.storage_manager.get('teams')}")
        round_length = self.app.storage_manager.get_value('round_length')
        self.ids.timer_bar.value = round_length
        self.ids.timer_label.text = str(round_length)
        team_name = self.app.storage_manager.get_value('teams')[self.current_team_index]['name']
        self.ids.team_label.text = f"Komanda: {team_name}"
        self.show_new_word()

    def start_game(self):
        Clock.schedule_interval(self.start_timer, 1)
        self.ids.start_game_btn.disabled = True

    def start_timer(self, *args):
        self.ids.timer_bar.value -= 1
        current_length = self.ids.timer_bar.value
        self.ids.timer_label.text = str(current_length)

    def add_score(self):
        self.app.storage_manager.set_value('teams')[self.current_team_index]['total_score'] += 1
        print(self.app.storage_manager.get_value('teams')[self.current_team_index]['total_score'])
    
    def show_new_word(self):
        self.ids.guess_word.text = random.choice(self.words)
