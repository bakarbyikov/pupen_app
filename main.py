__version__ = "0.1.0"

import kivy

kivy.require('2.3.0')

from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class WriteIt(Widget):
    text_box = ObjectProperty(None)
    talk_button = ObjectProperty(None)
    hello_sound = SoundLoader.load('sounds/pupen.wav')
    hello_sound.volume = 0.5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_text(self):
        self.hello_sound.play()
        self.text_box.text *= 2

class OlegApp(App):
    
    def build(self):
        app = WriteIt()
        return app

if __name__ == '__main__':
    OlegApp().run()