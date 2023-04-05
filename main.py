import os

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons

from View.AppLayout.app_layout import AppLayout
from View.common.helpers.storage_manager import StorageManager
from View.common.helpers.game_manager import GameManager

# Setup

Window.size = (400, 700)

class ExplainWordsGame(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Styling
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.set_colors(
            "Purple", "300", "100", "400", # Primary colors
            "Pink", "300", "100", "400"    # Accent
        )
        self.fonts = {
            "telegraf":       "assets/fonts/telegraf-regular.otf",
            "telegraf-light": "assets/fonts/telegraf-light.otf",
            "telegraf-bold":  "assets/fonts/telegraf-bold.otf"
        }
        self.icons = list(md_icons.keys())
        # Logic / App
        self.storage_manager = StorageManager()
        self.game_manager = GameManager()
        self.start_screen_path = os.path.join("View", "AppLayout", "app_layout.kv")

    def build(self):
        Builder.load_file(self.start_screen_path)
        return AppLayout()

# Run App

ExplainWordsGame().run()