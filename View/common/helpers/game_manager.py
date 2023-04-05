from kivymd.app import MDApp
from kivymd.toast import toast

import random

class GameManager:
    '''Manage the game, teams, rounds and game words.'''

    def __init__(self) -> None:
        self.app = MDApp.get_running_app()
        self.all_words = []
        self.played_words = []
        self.max_rounds = 4
        self.all_teams = {}
        self.round_number = 1
        self.team_index = 0
        self.current_team = None
        self.current_turn = None
        self.adult_mode = False
        self.reset_words()

    ### Game control

    def new_game(self):
        self.current_team = self.get_team_by_index(self.team_index)
        self.current_turn = Turn(self.round_number)

    def reset_game(self, keep_teams: bool = True):
        if keep_teams:
            for team in self.all_teams.values():
                team.reset_score()
        else:
            self.all_teams = {}
        self.reset_words()
        self.played_words = []
        self.round_number = 1
        self.team_index = 0
        self.current_team = None
        self.current_turn = None

    def next_round(self):
        self.round_number += 1
        self.team_index = 0
        self.new_game()

    # After screen actions

    def after_team_creation_screen(self):
        self.new_game()
        self.app.root.go_to("Game")

    def after_game_screen(self):
        self.app.root.go_to("Round Statistics")

    def after_statistics_screen(self):
        # Save previous round details
        self.current_team.add_round_details(self.round_number, self.current_turn)
        # Prepare for next round or round results
        self.team_index += 1
        target_screen = "Game"
        if self.team_index >= len(self.all_teams):
            target_screen = "Round Results"
        else:
            self.new_game()
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

    def add_team(self, team_name: str, icon: str = ''):
        self.all_teams[team_name] = Team(team_name, icon)

    def remove_team(self, team_name: str):
        del self.all_teams[team_name]

    def get_team_by_index(self, team_index: int):
        all_teams = list(self.all_teams.values())
        if team_index < len(all_teams):
            return all_teams[team_index]
        else:
            print(f"Team index out of bounds: '{self.team_index}'")
            return None

    def get_team_by_name(self, team_name: str):
        return self.all_teams[team_name]
    
    def get_sorted_teams(self, round_number: int = -1):
        all_team_details = []
        for team in self.all_teams.values():
            team_details = []
            team_details.append(team.name)
            team_details.append(team.icon)
            score = team.total_score if round_number == -1 else team.get_round_score(round_number)
            team_details.append(str(score))
            all_team_details.append(team_details)

        sorted_details = sorted(all_team_details, key=lambda x: x[2], reverse=True)
        return sorted_details

    ### Game word control
        
    def get_new_word(self, remove_word: bool = False):
        if len(self.all_words) > 0:
            chosen_word = random.choice(self.all_words)
            if remove_word: self.all_words.remove(chosen_word)
            return chosen_word
        else:
            toast('Visi vārdi izspēlēti!')
            return -1
        
    def reset_words(self):
        self.all_words = self.app.storage_manager.get_game_words(self.adult_mode)

### Turn

class Turn:
    '''Represents a single turn in a round for a single team.'''

    def __init__(self, round_number: int):
        self.round_number = round_number
        self.all_words = []
        self.guessed_words = []
        self.skipped_words = []
        self.score = 0

    # Handle words thats were skipped and later guessed
    def save_word(self, word: str, guessed: bool):
        word_pair = [word, guessed]
        if word_pair not in self.all_words: self.all_words.append(word_pair)
        if guessed and word not in self.guessed_words:
            self.guessed_words.append(word)
            self.score += 1
        elif not guessed and word not in self.skipped_words:
            self.skipped_words.append(word)

    def edit_word(self, word: str, guessed: bool):
        # Edit all words list
        for idx, word_pair in enumerate(self.all_words):
            if word in word_pair:
                self.all_words[idx][1] = guessed
                break

        # Edit guessed/skipped lists
        if guessed:
            index = self.skipped_words.index(word)
            del self.skipped_words[index]
            self.guessed_words.append(word)
            self.score += 1
        else:
            index = self.guessed_words.index(word)
            del self.guessed_words[index]
            self.skipped_words.append(word)
            self.score -= 1

    def get_all_words(self):
        return [x[0] for x in self.all_words]

### Team

class Team:
    '''Represents a single team.'''

    def __init__(self, name: str, icon: str = ''):
        self.name = name
        self.round_details = {}
        self.total_score = 0
        self.icon = icon

    def get_round_score(self, round_number):
        return self.round_details[str(round_number)].score
    
    def add_round_details(self, round_number, turn: Turn):
        self.round_details[str(round_number)] = turn
        self.total_score += turn.score
    
    def reset_score(self):
        self.round_details = {}
        self.total_score = 0
