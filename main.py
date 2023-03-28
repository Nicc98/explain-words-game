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

app_colors = {
    "LightPurple": "#E1DEF8",
    "Purple":      "#CFAFF1",
    "DarkPurple":  "#9A72D5",
    "LightBlue":   "#75E1ED",
    "Blue":        "#D4E4FF",
    "DarkBlue":    "#82B4DF"
}

class ExplainWordsGame(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Styling
        self.app_colors = app_colors
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