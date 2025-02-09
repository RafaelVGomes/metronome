from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from src.components.tick import Tick

class MetronomeUI(BoxLayout):
  is_metronome_running: bool = BooleanProperty(False)

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.tick_handler = Tick()
    
  def toggle_metronome(self) -> None:
    """Toggles the metronome by calling Tick."""
    self.tick_handler.toggle()
    self.is_metronome_running = self.tick_handler.is_running
    
  
  def get_bpm(self) -> int:
    """Returns the current BPM."""
    return self.tick_handler.bpm

  def set_bpm(self, bpm: int) -> None:
    """Sets the BPM."""
    self.tick_handler.bpm = bpm

  # def is_metronome_running(self) -> bool:
  #   """Checks if the metronome is running."""
  #   return self.tick_handler.is_running()