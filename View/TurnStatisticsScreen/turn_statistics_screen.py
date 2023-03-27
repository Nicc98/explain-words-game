from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp

class TurnStatisticsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.populate_turn_word_list()

    def on_leave(self, *args):
        self.ids.turn_word_list.clear_widgets()

    def continue_game(self):
        self.app.game_manager.after_statistics_screen()

    def populate_turn_word_list(self):
        all_words = self.app.game_manager.current_turn.all_words
        
        for word in all_words:
            played_word = OneLineIconListItem(
                text = f"{word[0]}: {word[1]}",
                text_color = "#ffffff"
            )
            self.ids.turn_word_list.add_widget(played_word)