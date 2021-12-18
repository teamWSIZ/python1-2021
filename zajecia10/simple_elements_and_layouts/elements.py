from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from PIL import Image


class Root(BoxLayout):
    pass

class Second(BoxLayout):
    def print_something(self):
        print('OK')


class ElementsApp(App):
    kv_directory = '.'


if __name__ == '__main__':
    ElementsApp().run()
