from kivymd.uix.screen import MDScreen

class AppLayout(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_to(self, screen_name: str, transition_direction = 'left'):
        print(f"Going to '{screen_name}' screen...")
        self.ids.screen_manager.current = screen_name
        self.ids.screen_manager.transition.direction = transition_direction
        