from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from urllib.parse import urlparse


class TestApp(App):

    def build(self):

        self.window = GridLayout() #tinklelio išdėstymas
        Window.clearcolor = '#D0D0D0'
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7) # margin syze
        self.window.pos_hint = {'center_x':0.5, 'center_y':0.5}

        self.window.add_widget(Image(source='YouTube.png')) # up image

        self.greeting = Label(
                        text='Suveskite URL adresą?',
                        font_size = 18,
                        color = '#000000'
                        ) # Text
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline=False,
                    padding_y = (20,20),
                    size_hint = (1, 0.5)
                    ) # Input
        self.window.add_widget(self.user)
        #self.result = urlparse(self.user)

        self.button = Button(
                    text='OK',
                    size_hint = (1, 0.5),
                    bold = True,
                    background_color = '#D0D0D0',
                    background_normal = '' #Spalvu pasvieisnimui
                    )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window



    def callback(self, instance):
        result = urlparse(self.user.text)
        http = result.scheme
        yt = result.netloc
        if http != 'https':
            self.greeting.text = 'This is not URL. Try again'
        elif yt != 'www.youtube.com':
            self.greeting.text = 'This is not Youtube URL'
        else:
            self.greeting.text = self.user.text

if __name__ == '__main__':
    TestApp().run()

