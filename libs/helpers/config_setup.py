from kivy.config import Config
import os

class ConfigSetup():

    def __init__(self) -> None:
        self.logs_dir = "logs"

    def change_screen_size(self, width: int = 400, height: int = 700):
        '''
        Change App screen size \n
        Set to False for dynamic sizes
        '''
        Config.set('graphics', 'width', f'{width}')
        Config.set('graphics', 'height', f'{height}')
        Config.write()
    
    def toggle_debug(self, debug: bool = True):
        '''Enable or disable debugging'''
        if not debug:
            return
        
        Config.add_section('Logging')
        Config.set('Logging', "log file",  os.path.join(self.logs_dir, 'app.log'))

        Config.set('Logging', "logging", 1)
        Config.set('Logging', "console logging", 1)
        Config.set('Logging', "console log level", "DEBUG")
        Config.set('Logging', "file log level", "DEBUG")
        Config.set('Logging', "file logging", 1)