from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem

from kivy.properties import BooleanProperty, StringProperty

app = MDApp.get_running_app()

###
# Box layouts
###

class MainBox(MDBoxLayout):
    pass

class TopBoxMainV(MDBoxLayout):
    pass

class TopBoxMainH(MDBoxLayout):
    pass

class TopBoxSideV(MDBoxLayout):
    pass

class TopBoxMiddleV(MDBoxLayout):
    pass

class MiddleBoxV(MDBoxLayout):
    pass

class MiddleBoxH(MDBoxLayout):
    pass

class BottomBoxV(MDBoxLayout):
    pass

class BottomBoxH(MDBoxLayout):
    pass

###
# Buttons
###

class RoundTextButton(MDRoundFlatButton):
    pass

class TopLeftButton(MDIconButton):
    pass

class TopRightButton(MDIconButton):
    pass

class SkipButton(MDIconButton):
    pass

class GuessButton(MDIconButton):
    pass

###
# Labels
###

class HeaderLabel(MDLabel):
    pass

class SubHeaderLabel(MDLabel):
    pass

class TextLabel(MDLabel):
    pass

###
# List items
###

class RightContainerTouch(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

class TeamListItem(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()

    def delete_item(self, *args):
        # Remove team from screen
        team_list = self.parent # list
        team_list.remove_widget(self)
        # Remove team from game manager
        app.game_manager.remove_team(self.text)

class ScoreListItem(OneLineAvatarIconListItem):
    text = StringProperty()
    icon = StringProperty()
    score = StringProperty()

class WordListItem(OneLineAvatarIconListItem):
    text = StringProperty()
    guessed = BooleanProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_switch_active(self, value):
        app.game_manager.current_turn.edit_word(self.text, value)
            