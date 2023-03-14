from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem

class OptionsNavigationDrawer(MDBoxLayout):
    pass

class OptionsItem(OneLineIconListItem):
    icon = StringProperty()
    text = StringProperty()
    values = ListProperty()
