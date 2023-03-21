import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from View.AppLayout.app_layout import AppLayout
from View.common.helpers.storage_manager import StorageManager
from View.common.helpers.game_manager import GameManager

# Setup

Window.size = (400, 700)

class ExplainWordsGame(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Styling
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.material_style = "M3"
        self.theme_cls.set_colors(
            "Orange", "300", "100", "400", # Primary colors
            "Teal", "300", "100", "400"    # Accent
        )
        # Logic / App
        self.storage_manager = StorageManager()
        self.game_manager = GameManager()
        self.start_screen_path = os.path.join("View", "AppLayout", "app_layout.kv")

    def build(self):
        Builder.load_file(self.start_screen_path)
        return AppLayout()

# Run App

ExplainWordsGame().run()