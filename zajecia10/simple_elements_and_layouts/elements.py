from kivy.app import App
from kivy.core.text import Label
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from PIL import Image


# todo: windows on VM hack (via Mesa3D)
# import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class MainWidget(BoxLayout):
    # class of the root widget
    pass


class BottomMenu(BoxLayout):
    xxx = ObjectProperty(None)
    input_ = ObjectProperty(None)

    def print_something(self):
        print('OK')

    def new_function(self):
        print('new text!!!')

    def compute_square_from_input(self, text):
        print(f'w polu napisano: {text}')
        x = int(text)
        # print(f'square = {x**2}')
        # print(self.xxx.text)
        self.xxx.text = f'wynik: {x**2}'


# https://kivy.org/doc/stable/guide/lang.html
class ElementsApp(App):
    # główna klasa kivy
    kv_directory = '.'  # tu szuka elements.kv, MyApp -> my.kv


if __name__ == '__main__':
    ElementsApp().run()
