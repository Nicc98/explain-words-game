from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore

from libs.baseclass.app_layout import AppLayout
from libs.helpers.config_setup import ConfigSetup
from libs.helpers.data_helper import StorageHelper

class ExplainWordsGame(MDApp):

    def build(self):
        self.storage = JsonStore('explain_words_game.json')
        self.storage_helper = StorageHelper(storage = self.storage)
        self.storage_helper.load_colors()
        Builder.load_file("main.kv")
        return AppLayout()
    
    def load_colors(self):
        self.storage
    
if __name__ == "__main__":

    config = ConfigSetup()
    config.change_screen_size()

    ExplainWordsGame().run()