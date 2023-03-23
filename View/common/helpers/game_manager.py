from kivymd.app import MDApp

import random

GAME_WORDS = [
    "Abols", "Kaposts", "Pica", "Saldejums",
    "Burgers", "Burrito", "Zupa", "Sacepums"
]

class GameManager:
    '''Manage the game, teams, rounds and game words.'''

    def __init__(self) -> None:
        self.app = MDApp.get_running_app()
        self.all_words = GAME_WORDS.copy()
        self.played_words = []
        self.max_rounds = 4
        self.all_teams = {}
        self.round_number = 1
        self.team_index = 0
        self.current_team = None
        self.current_turn = None

    ### Game control

    def new_game(self):
        self.current_team = self.get_team_by_index(self.team_index)
        self.current_turn = Turn(self.round_number)

    def reset_game(self, keep_teams: bool = True):
        if not keep_teams: self.all_teams = {}
        self.all_words = GAME_WORDS.copy()
        self.played_words = []
        self.round_number = 1
        self.team_index = 0
        self.current_team = None
        self.current_turn = None

    def next_turn(self):
        self.team_index += 1  
        self.current_team = self.get_team_by_index(self.team_index)
        self.current_turn = Turn(self.round_number)
        # Remove this after testing / getting more words
        self.all_words = GAME_WORDS.copy()

    def next_round(self):
        self.round_number += 1
        self.team_index = 0

    # After screen actions

    def after_team_creation_screen(self):
        self.new_game()
        self.app.root.go_to("Game")

    def after_game_screen(self):
        self.app.root.go_to("Round Statistics")

    def after_statistics_screen(self):
        self.next_turn()
        target_screen = "Game"
        if self.team_index == len(self.all_teams):
            target_screen = "Round Results"
        self.app.root.go_to(target_screen)

    def after_round_results_screen(self):
        self.next_round()
        target_screen = "Game"
        if self.round_number > self.max_rounds:
            target_screen = "Game Results"
        self.app.root.go_to(target_screen)

    def after_game_results_screen(self):
        self.reset_game()
        self.app.root.go_to("Home")

    ### Team control

    def add_team(self, team_name: str):
        self.all_teams[team_name] = Team(team_name)

    def get_team_by_index(self, team_index: int):
        all_teams = list(self.all_teams.values())
        if team_index < len(all_teams):
            return all_teams[team_index]
        else:
            print(f"Team index out of bounds: '{self.team_index}'")
            # Maybe just return team with index 0 to simplify the loop
            return None

    def get_team_by_name(self, team_name: str):
        return self.all_teams[team_name]

    ### Game word control
        
    def get_new_word(self, remove_word: bool = False):
        if len(self.all_words) > 0:
            chosen_word = random.choice(self.all_words)
            if remove_word: self.all_words.remove(chosen_word)
            return chosen_word
        else:
            print("Out of words!")
            return -1

### Turn

class Turn:
    '''Represents a single turn in a round for a single team.'''

    def __init__(self, round_number: int):
        self.round_number = round_number
        self.all_words = []
        self.guessed_words = []
        self.skipped_words = []
        self.score = 0

    def save_word(self, word: str, guessed: bool):
        word_pair = [word, guessed]
        if word_pair not in self.all_words: self.all_words.append(word_pair)
        if guessed and word not in self.guessed_words:
            self.guessed_words.append(word)
            self.score += 1
        elif not guessed and word not in self.skipped_words:
            self.skipped_words.append(word)

    def edit_words(self, edited_words: list):
        for index, edited_word in enumerate(edited_words):
            if self.all_words[index] != edited_word:
                self.all_words[index] = edited_word

    def get_all_words(self):
        return map(lambda x: x[0], self.all_words)

### Team

class Team:
    '''Represents a single team.'''

    def __init__(self, name: str):
        self.name = name
        self.round_details = {}
        self.total_score = 0

    def get_round_score(self, round_number):
        return self.round_details[str(round_number)].score
    
    def add_round_details(self, round_number, turn: Turn):
        self.round_details[str(round_number)] = turn
        self.total_score += turn.score
