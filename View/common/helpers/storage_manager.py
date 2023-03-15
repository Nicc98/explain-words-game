from kivy.storage.jsonstore import JsonStore

class StorageManager():
    '''Store and manage app data.'''

    def __init__(self) -> None:
        self.storage = JsonStore('explain_words_game.json')
        self.load_default_values()

    def load_default_values(self):
        self.set_value('blue', (0.36, 0.41, 0.57, 1))
        self.set_value('light_blue', (0.55, 0.51, 0.62, 1))
        self.set_value('pink', (0.9, 0.8, 0.8, 1))
        self.set_value('light_pink', (0.89, 0.8, 0.75, 1))

    def get(self, key: str):
        return self.storage.get(key)

    def get_color(self, color_name: str):
        return self.get_value(color_name)
    
    def get_value(self, key: str):
        return self.storage.get(key)['value']

    def set_value(self, key: str, value):
        self.storage.put(key, value = value)

    def delete_value(self, key: str):
        self.storage.delete(key)