__version__ = "0.1.0"

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock


class WriteIt(Widget):
    pass


class OlegApp(App):
    def update_text(self):
        print("Hello")


    def build(self):
        game = WriteIt()
        return game


if __name__ == '__main__':
    OlegApp().run()