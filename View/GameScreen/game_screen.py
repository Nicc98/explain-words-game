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
        # Timing
        self.round_length = 60 # in seconds
        self.timer_tick = 1
        # game instance
        self.game_ongoing = False
        self.current_team_index = 0
        self.current_team_score = 0
        # Words
        self.words = [
            "Abols", "Kaposts", "Pica", "Saldejums",
            "Burgers", "Burrito", "Zupa", "Sacepums"
        ]
        self.max_words = 8
        self.words_pulled = 0
    
    def on_enter(self, *args) -> None:
        self.ids.timer_label.text = str(self.round_length)
        team_name = self.app.storage_manager.get_value('teams')[self.current_team_index]['name']
        self.ids.team_label.text = team_name

    def start_game(self):
        self.game_ongoing = True
        self.show_new_word()
        self.timer_tick = self.round_length / 100 / 10
        Clock.schedule_interval(self.start_timer, 0.1)
        self.ids.start_game_btn.disabled = True

    def start_timer(self, *args):
        if not self.game_ongoing: return
        self.ids.timer_bar.value -= self.timer_tick
        current_length = self.ids.timer_bar.value
        self.ids.timer_label.text = str(int(current_length))
            
        match current_length:
            case 30:
                self.ids.timer_bar.color = (0.1, 0.5, 0.5, 0.7)

            case 15:
                self.ids.timer_bar.color = (1, 0, 0, 0.7)

            case 0:
                self.game_ongoing = False
    
    def add_score(self):
        if not self.game_ongoing: return
        self.current_team_score += 1
        print(f"Score: {self.current_team_score}")
        self.show_new_word()
    
    def show_new_word(self):
        if not self.game_ongoing: return
        self.ids.guess_word.text = random.choice(self.words)

    def on_exit(self):
        # score = self.app.storage_manager.get_value('teams')[self.current_team_index]['total_score']
        # self.app.storage_manager.set_value('teams', value[])[self.current_team_index]['total_score'] += 1
        # print(self.app.storage_manager.get_value('teams')[self.current_team_index]['total_score'])

    ###

    # def animate_widget_removal(self, wid):
    #     # animate shrinking widget width
    #     anim = Animation(width=0)
    #     anim.bind(on_complete=self.do_actual_remove)
    #     anim.start(wid)

    # def remove_word_card(self, anim, wid):
    #     # actually remove the shrunken widget
    #     self.root.ids.order_list.remove_widget(wid)

    # def add_word_card(self,image):
    #     i = Item()
    #     i.image=image
    #     i.opacity = 0
    #     self.ids.order_list.add_widget(i)
    #     anim = Animation(opacity=1)
    #     anim.start(i)