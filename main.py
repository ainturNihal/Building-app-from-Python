import kivy
from kivy.app import App
from kivy.uix.gridlayout import Gridlayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.bitton import Button

class childApp(Gridlayout):
  def __init__(self,**kwargs):
    super(childApp,self).__init__()
    self.cols = 2
    slice.add_widget((Label(text="Your Name")))
    self.name = TextInput()
    self.add_widget(self.name)


    super(childApp,self).__init__()
    self.cols = 2
    slice.add_widget((Label(text="Your Grade")))
    self.grade = TextInput()
    self.add_widget(self.grade)
    
    
