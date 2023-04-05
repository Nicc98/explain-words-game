from kivy.storage.jsonstore import JsonStore

class StorageManager():
    '''Store and manage app data.'''

    def __init__(self) -> None:
        self.storage = JsonStore('explain_words_game.json')

    def load_default_values(self):
        self.set_value('key', 'value')
    
    def get_value(self, key: str):
        return self.storage.get(key)['value']

    def set_value(self, key: str, value):
        self.storage.put(key, value = value)

    def delete_value(self, key: str):
        self.storage.delete(key)

    # Game words

    def get_game_words(self, adult_mode: bool = False):
        all_words = []
        all_words.extend(self.get_value("darbibas_vardi"))
        all_words.extend(self.get_value("ipasibas_vardi"))
        all_words.extend(self.get_value("citi_vardi"))
        if adult_mode: all_words.extend(self.get_value("rupjie_vardi"))
        return all_words