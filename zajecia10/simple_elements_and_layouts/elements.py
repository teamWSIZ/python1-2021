from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from PIL import Image
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class Root(BoxLayout):
    pass

class Second(BoxLayout):
    text_ouput = ObjectProperty(None)

    def print_something(self):
        print('OK')

    def new_function(self):
        print('new text')

    def compute_square_from_input(self, text):
        print(f'w polu napisano: {text}')
        # x = int(text)
        # print(f'square = {x**2}')
        print(self.ids)
        # self.text_ouput.text = f'wynik: {x**2}'


class ElementsApp(App):
    kv_directory = '.'


if __name__ == '__main__':
    ElementsApp().run()
