from kivy.app import App
from src.gui.metronomeUI import MetronomeUI


class MetronomeApp(App):
  def build(self) -> MetronomeUI:
    return MetronomeUI()