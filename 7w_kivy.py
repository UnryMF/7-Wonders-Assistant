##############################
#    7 Wonders Assistant     #
##############################

import kivy
import self as self
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import csv


kivy.require('1.11.1')


class WManager(BoxLayout, Screen):

    player_names = []
    pp1 = ObjectProperty(None)
    pp2 = ObjectProperty(None)
    pp3 = ObjectProperty(None)
    pp4 = ObjectProperty(None)
    pp5 = ObjectProperty(None)
    pp6 = ObjectProperty(None)
    pp7 = ObjectProperty(None)
    pp8 = ObjectProperty(None)

    w0 = ['the Great Pyramid of Giza', 'the Colossus of Rhodes', 'the Lighthouse of Alexandria',
          'the Mausoleum at Halicarnassus', 'the Temple of Artemis', 'the Statue of Zeus',
          'the Hanging Gardens of Babylon']
    wf = []

    def __init__(self, **kwargs):
        super(WManager, self).__init__(**kwargs)

    def player_set(self):
        # Add value from boxes to player_names list
        self.player_names.append(self.pp1.text)
        self.player_names.append(self.pp2.text)
        self.player_names.append(self.pp3.text)
        self.player_names.append(self.pp4.text)
        self.player_names.append(self.pp5.text)
        self.player_names.append(self.pp6.text)
        self.player_names.append(self.pp7.text)
        self.player_names.append(self.pp8.text)
        # Remove blanks
        while '' in self.player_names:
            self.player_names.remove('')

    # function taken from https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
    def append_new_line(self, file_name, text_to_append):
        with open(file_name, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(text_to_append)

    def randomizer(self):
        # additional conditions to be added:
        # if Advanced.varA and Advanced.VarB are False = warning message
        # if player8 is populated then at least Armanda/Cities have to be checked
        # establish file management to create new files for session / loads previous sessions with scores (later on)
        with open('test.txt', 'a') as ResultsScreen.display:
            for self.i in self.player_names:
                self.wonder = random.choice(self.w0)
                self.add = self.i + ' will play ' + self.wonder + ' (' + random.choice(AdvancedWindow.ab) + ')'
                # print(self.i, ' will play ', self.wonder, '(', random.choice(AdvancedWindow.ab), ')')
                self.append_new_line('test.txt', str(self.add))
                self.w0.remove(self.wonder)

    def next_btn(self):
        self.player_set()
        # print(self.player_names)
        self.randomizer()


class WindowManager(ScreenManager):
    pass


class AdvancedWindow(BoxLayout, Screen):
    ab = ['A', 'B']
    varA = ObjectProperty(None)
    varB = ObjectProperty(None)
    wf = []
    wl = ObjectProperty(None)
    wc = ObjectProperty(None)
    wp = ObjectProperty(None)
    wa = ObjectProperty(None)
    wo1 = ObjectProperty(None)
    wo2 = ObjectProperty(None)

    def checkbutton_a(self):
        if self.varA is False:
            self.ab.remove('A')
        else:
            self.ab.append('A')

    def checkbutton_b(self):
        if self.varB is False:
            self.ab.remove('B')
        else:
            self.ab.append('B')

    def checkbutton_wl(self):
        if self.wl is False:
            WManager.w0.remove('the Colosseum of Rome')
        else:
            WManager.w0.append('the Colosseum of Rome')

    def checkbutton_wc(self):
        if self.wl is False:
            WManager.w0.remove('the Hagia Sophia of Byzantium')
            WManager.w0.remove('Al Khazneh of Petra')
        else:
            WManager.w0.append('the Hagia Sophia of Byzantium')
            WManager.w0.append('Al Khazneh of Petra')

    def checkbutton_wp(self):
        if self.wp is False:
            WManager.w0.remove('Abu Simbel')
            WManager.w0.remove('the Great Wall of China')
            WManager.w0.remove('Stonehenge')
            WManager.w0.remove('The Manneken Pis of Brussels')
        else:
            WManager.w0.append('Abu Simbel')
            WManager.w0.append('the Great Wall of China')
            WManager.w0.append('Stonehenge')
            WManager.w0.append('The MAnneken Pis of Brussels')

    def checkbutton_wa(self):
        if self.wa is False:
            WManager.w0.remove('Siracusa')
        else:
            WManager.w0.append('Siracusa')

    def checkbutton_wo1(self):
        if self.wo1 is False:
            WManager.w0.remove('the Manneken Pis of Brussels')
        else:
            WManager.w0.append('the Manneken Pis of Brussels')

    def checkbutton_wo2(self):
        if self.wo1 is False:
            WManager.w0.remove('the Settlers of Catan')
        else:
            WManager.w0.append('the Settlers of Catan')
    pass


class ResultsScreen(BoxLayout, Screen):

    def __init__(self, **kwargs):
        super(ResultsScreen, self).__init__(**kwargs)

        with open('test.txt', 'r') as self.display:
            self.display_contents = self.display.read()
            # print(self.display_contents)

    display_contents = StringProperty('default')

    pass


# App executive class
kv = Builder.load_file("my.kv")


class MyMainApp(App):
    title = '7 Wonders Assistant'

    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()