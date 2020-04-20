import kivy
from kivy.app import App
from kivy.uix.label import Label


class FrontEnd(App):
    def build(self):
        root_widget = Label(text="Hello, World!")
        return root_widget


FrontEnd().run()
