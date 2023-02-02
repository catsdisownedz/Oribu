from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class AnchorLayout(AnchorLayout):
    pass

class BoxLayout(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text = "Criminal Prediction")
        b2 = Button(text = "Click here for more")
        self.add_widget(b1)
        self.add_widget(b2)
"""
class MainWidget (Widget):
    pass

class CrimeApp (App):
    pass



CrimeApp().run()
