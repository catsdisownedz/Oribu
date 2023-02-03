'''from plyer import notification

notification.notify(
    title = 'testing',
    message = 'message',
    app_icon = None,
    timeout = 10,
)
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from plyer import notification

def callback():
    notification.notify(
        title = 'testing',
        message = 'message',
        app_icon = None,
        timeout = 10,)

class AnchorLayout(AnchorLayout):
    pass

class Box(BoxLayout):
    def button_click(self):
        print(callback())

    '''def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "Criminal Prediction")
        b2 = Button(text = "Click here for more")
        b2.bind(on_press = callback)
        self.add_widget(b1)
        self.add_widget(b2)
    '''
class MainWidget (Widget):
    pass
    

class CrimeApp (App):
    pass

    
CrimeApp().run()
