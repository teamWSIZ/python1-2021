"""
Application built from a  .kv file
==================================

This shows how to implicitly use a .kv file for your application. You
should see a full screen button labelled "Hello from test.kv".

After Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is
TestApp, which implies that kivy should try to load "test.kv". That file
contains a root Widget.
<<<<<<< HEAD:zajecia10/simple/simple.py
"""
=======
'''

import kivy
# import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

kivy.require('1.0.7')

>>>>>>> ddf80cd9d6f659743465c31c8ed2f93726911588:zajecia10/with_kv/app_with_kv.py
from kivy.app import App


class TestApp(App):
    kv_directory = '.'


if __name__ == '__main__':
    TestApp().run()
