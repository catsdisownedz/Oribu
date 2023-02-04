from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from plyer import notification
import logging

def notif_log():
    log = logging.getLogger("Notifications")
    handler = logging.FileHandler('Notifications.log')
    formatter = logging.Formatter('%(asctime)s\n %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)

    log.info("test custom")

'''def crim_sighting():
    name = name
    security_risk = risk_level
    icon = security risk dependant (changes color depending on risk)
'''

def callback():
    notification.notify(
        title = 'Criminal Activity',
        message = 'Criminal Sighted',
        # message = crim_sighting(),
        app_icon = r"C:\Users\nadam\OneDrive\Documents\GitHub\Obiru\police-badge.ico",
        timeout = 10,)
    
    

def button_click(self):
    print(callback())
    
class Homepage(ScrollView):
     #if isIdentified = True:  
     #print(callback()) 
    def button_click(self):
        print(callback()) 

class Stack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #b1 = Button(text = "Criminal Prediction")
        #b2 = Button(text = "Click here for more")
        #b2.bind(on_press = callback)
        #self.add_widget(b1)
        #self.add_widget(b2)

class Log(ScrollView):
    print(notif_log())


class Anchor(AnchorLayout):
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

  #if isIdentified = True:  
  #     print(callback()) 

CrimeApp().run()
