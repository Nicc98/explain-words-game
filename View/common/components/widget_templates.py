from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem

###
# Box layouts
###

class MainBox(MDBoxLayout):
    pass

class TopBoxV(MDBoxLayout):
    pass

class TopBoxH(MDBoxLayout):
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
    pass

class ScoreListItem(OneLineAvatarIconListItem):
    pass

class WordListItem(OneLineAvatarIconListItem):
    pass