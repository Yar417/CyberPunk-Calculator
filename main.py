from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivymd.theming import ThemeManager
from kivymd.app import MDApp

Window.size = (320, 450)


class Container(GridLayout):
    a = ''
    b = ''
    act = ''

    def append(self, number):
        if self.label_text.text == 'Error!':
            self.label_text.text = ''

        if number == 0 and self.label_text.text == "0":
            return
        elif number == 'C':
            self.label_text.text = ''
            self.a = ''
            self.b = ''
            return
        if number != '.':
            self.label_text.text += str(number)
        elif number == '.':
            if number in self.label_text.text:
                return
            if self.label_text.text != "":
                self.label_text.text += str(number)

            elif self.label_text.text == '':
                self.label_text.text += '0.'

        if self.a != '':
            self.b += str(number)



    def action(self, to_do):
        if to_do == '+' or to_do == '-' or to_do == '*' or to_do == '/':
            self.a = self.label_text.text
            self.label_text.text = ''
            self.act = to_do

        if to_do == '=':
            if self.b == '' or self.b == '.':
                return
            if self.act == '+':
                self.label_text.text = str(float(self.a) + float(self.b))

            elif self.act == '-':
                self.label_text.text = str(float(self.a) - float(self.b))

            elif self.act == '*':
                self.label_text.text = str(float(self.a) * float(self.b))

            elif self.act == '/':
                try:
                    self.label_text.text = str(float(self.a) / float(self.b))
                except Exception:
                    self.label_text.text = 'Error!'
                    self.a = ''
                    self.b = ''

            self.a = self.label_text.text
            self.b = ''


class CuberPunkCalc(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        music = SoundLoader.load('files/1.mp3')
        if music:
            music.play()
        return Container()


if __name__ == '__main__':
    CuberPunkCalc().run()
