from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from View.common.components.widget_templates import RoundTextButton

class GameScreen(MDScreen):

    # TODO Add hard mode toggle switch in settings:
    # If enabled then when a word is skipped, 5 (or other amount)
    # of seconds get removed from the timer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.game_ongoing = False
        self.counter = 0
        self.current_word = "- - -"
        self.dialog = MDDialog(
            text = "Laiks beidzies!",
            auto_dismiss = False,
            buttons = [
                MDRaisedButton(
                    text = 'Turpināt',
                    on_release = self.go_to_turn_statistics
                )
            ]
        )

        self.start_btn = RoundTextButton(
            id = "start_turn_btn",
            text = "Sākt",
            on_release = self.start_turn
        )
    
    def on_pre_enter(self, *args):
        self.ids.header_label.text = f"{self.app.game_manager.round_number}. kārta"
        self.ids.team_label.text = self.app.game_manager.current_team.name
        self.ids.bottom_layout.add_widget(self.start_btn)
        self.ids.timer_label.text = "60"
        self.ids.timer_bar.value = 60
        self.ids.word_skipped_btn.disabled = False
        self.ids.word_guessed_btn.disabled = False    

    ### Handle game updates

    def start_turn(self, instance_btn):
        self.game_ongoing = True
        self.show_new_word()
        # Start timer
        self.turn_timer = Clock.schedule_interval(self.update_turn, 0.1)
        # Disable elements
        self.ids.bottom_layout.remove_widget(self.start_btn)        

    def update_turn(self, *args):
        if not self.game_ongoing: return

        self.ids.timer_bar.value -= 0.1
        current_time = self.ids.timer_bar.value
        # Check for stop
        if current_time <= 0: self.stop_turn_actions()
        # Update label
        self.handle_timer_label(current_time)
        # Update progress bar
        self.handle_timer_bar(current_time)

    def stop_turn_actions(self):
        self.ids.word_skipped_btn.disabled = True
        self.ids.word_guessed_btn.disabled = True
        self.turn_timer.cancel()
        self.game_ongoing = False
        self.ids.timer_label.text = "0"
        self.ids.timer_bar.value = 0
        self.ids.guess_word.text = "- - -"
        self.counter = 0
        self.show_turn_info()
    
    # Handle timer elements

    def handle_timer_label(self, current_time):
        self.counter += 1
        if self.counter == 10:
            self.counter = 0
            self.ids.timer_label.text = str(int(current_time))

    def handle_timer_bar(self, current_time):
        color_map = {
            0.25: "#FF0000",  # Red
            0.5:  "#FFFF00"  # Yellow
        }

        for threshold, color in color_map.items():
            if current_time / 60.0 <= threshold:
                self.ids.timer_bar.color = color
                break

    # Score and word updates

    def guess_word(self):
        if not self.game_ongoing: return
        self.save_word(True)
        self.show_new_word(True)

    def skip_word(self):
        if not self.game_ongoing: return
        self.save_word(False)
        self.show_new_word(True)

    def save_word(self, guessed: bool):
        if not self.game_ongoing: return
        self.app.game_manager.current_turn.save_word(self.current_word, guessed)
    
    def show_new_word(self, remove_word: bool = False):
        if not self.game_ongoing: return
        self.current_word = self.app.game_manager.get_new_word(remove_word)
        if self.current_word == -1:
            self.stop_turn_actions()
        else:
            self.ids.guess_word.text = self.current_word

    # Dialog

    def show_turn_info(self):
        self.dialog.open()
    
    def go_to_turn_statistics(self, instance_button):
        print(self.app.game_manager.current_turn.all_words)
        self.dialog.dismiss()
        self.app.game_manager.after_game_screen()
