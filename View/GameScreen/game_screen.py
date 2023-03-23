from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton

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
                    on_release = self.go_to_round_statistics
                )
            ]
        )
    
    def on_pre_enter(self, *args):
        self.ids.team_label.text = self.app.game_manager.current_team.name

    def start_round(self):
        self.game_ongoing = True
        self.show_new_word()
        # Start timer
        self.round_timer = Clock.schedule_interval(self.update_round, 0.1)
        # Disable elements
        self.ids.bottom_layout.remove_widget(self.ids.start_round_btn)

    ### Handle game updates

    def update_round(self, *args):
        if not self.game_ongoing: return

        self.ids.timer_bar.value -= 0.1
        current_time = self.ids.timer_bar.value
        # Check for stop
        if current_time <= 0: self.stop_round_actions()
        # Update label
        self.handle_timer_label(current_time)
        # Update progress bar
        self.handle_timer_bar(current_time)

    def stop_round_actions(self):
        self.ids.word_skipped_btn.disabled = True
        self.ids.word_guessed_btn.disabled = True
        self.round_timer.cancel()
        self.game_ongoing = False
        self.ids.timer_bar.value = 0
        self.ids.guess_word.text = "- - -"
        self.ids.timer_label.text = "0"
        self.counter = 0
        self.show_round_info()
    
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
        self.show_new_word()

    def save_word(self, guessed: bool):
        self.app.game_manager.current_turn.save_word(self.current_word, guessed)
    
    def show_new_word(self, remove_word: bool = False):
        if not self.game_ongoing: return

        self.current_word = self.app.game_manager.get_new_word(remove_word)
        if self.current_word == -1:
            self.stop_round_actions()
        else:
            self.ids.guess_word.text = self.current_word

    # Dialog

    def show_round_info(self):
        self.dialog.open()
    
    def go_to_round_statistics(self, instance_button):
        print(self.app.game_manager.current_turn.all_words)
        self.dialog.dismiss()
        self.app.game_manager.after_game_screen()
