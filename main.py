from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

import os

from View.AppLayout.app_layout import AppLayout
from View.common.helpers.storage_manager import StorageManager

# Setup

Window.size = (400, 700)

class ExplainWordsGame(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.theme_cls.material_style = "M3"
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Indigo"
        self.storage_manager = StorageManager()
        self.start_screen_path = os.path.join("View", "AppLayout", "app_layout.kv")

    def build(self):
        Builder.load_file(self.start_screen_path)
        return AppLayout()

# Run App

ExplainWordsGame().run()