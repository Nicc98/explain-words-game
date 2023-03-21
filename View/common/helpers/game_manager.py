import random

class GameManager:
    '''
    Manage teams with their names, round points and total points. \n
    Manage game words.
    '''

    def __init__(self) -> None:
        self.all_teams = {}
        self.words = [
            "Abols", "Kaposts", "Pica", "Saldejums",
            "Burgers", "Burrito", "Zupa", "Sacepums"
        ]

    ### Team control

    def add_team(self, team_name: str):
        self.all_teams[team_name] = Team(team_name)

    def get_team_by_index(self, team_index: int):
        return list(self.all_teams.values())[team_index]

    def get_team_by_name(self, team_name: str):
        return self.all_teams[team_name]

    def get_team_round_score(self, team_name: str, round_number: str):
        team = self.get_team_by_name(team_name)
        return team.round_details[round_number]

    def get_team_total_score(self, team_name: str):
        team = self.get_team_by_name(team_name)
        return team.total_score
    
    def add_team_round(self, team_name: str, round_number: str):
        team = self.get_team_by_name(team_name)
        team.round_details[round_number] = 0

    def increase_team_round_score(self, team_name: str, round_number: str):
        team = self.get_team_by_name(team_name)
        print("Score increase")
        print(f"Team: {team_name}, Round number: {round_number}")
        team.round_details[round_number] += 1 
        team.total_score += 1
        print(f"Round scores after: {team.round_details}")

    ### Game word control
        
    def get_new_word(self, remove_word: bool = False):
        if len(self.words) > 0:
            chosen_word = random.choice(self.words)
            if remove_word: self.words.remove(chosen_word)
            return chosen_word
        else:
            print("Out of words!")
            return -1

class Team:
    '''Represents a single team.'''

    def __init__(self, name: str):
        self.name = name
        self.round_details = {}
        self.total_score = 0

class Round:
    '''Represents a single round for 1 team'''

    def __init__(self, ):
        pass