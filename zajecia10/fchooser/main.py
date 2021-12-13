from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os

"""
Na Windows, szczególnie na VM, jest problem z OpenGL pokazującym wersję 1.1; 

Obejście: 
- wykorzystać Mesa3D, https://askubuntu.com/questions/1238523/enabling-opengl-in-windows-10-guest-vm-in-qemu
  (opowiedź usera Chris):
- ściągnąć https://github.com/pal1000/mesa-dist-win/releases i rozpakować
- uruchomić systemwidedeploy.cmd
- wybrać "1" z tego
-------------------------------------
Mesa3D system-wide deployment utility
-------------------------------------
Please make a deployment choice:
1. Core desktop OpenGL drivers
2. Core desktop OpenGL drivers + Intel swr
3. Install DirectX IL for redistribution only
(...)
- odkomentować linię poniżej

"""
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()