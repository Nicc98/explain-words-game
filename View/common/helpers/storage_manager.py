from kivy.storage.jsonstore import JsonStore

class StorageManager():
    '''Store and manage app data.'''

    def __init__(self) -> None:
        self.storage = JsonStore('explain_words_game.json')
        # self.load_default_values()

    def load_default_values(self):
        self.set_value('key', 'value')

    def get(self, key: str):
        return self.storage.get(key)
    
    def get_value(self, key: str):
        return self.storage.get(key)['value']

    def set_value(self, key: str, value):
        self.storage.put(key, value = value)

    def delete_value(self, key: str):
        self.storage.delete(key)