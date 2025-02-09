from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.widget import Widget
from src.components.sounds import SoundManager

from kivy.core.audio import SoundLoader
click1 = SoundLoader.load('assets/sounds/click1.wav')
click2 = SoundLoader.load('assets/sounds/click2.wav')

class Tick(Widget):
  bpm: NumericProperty = NumericProperty(60)
  is_running: BooleanProperty = BooleanProperty(False)
  beat_count: NumericProperty = NumericProperty(0)
  beats_per_measure: NumericProperty = NumericProperty(4)

  def __init__(self):
    super().__init__()
    # self.sound_manager = SoundManager()
  
  def toggle(self) -> None:
    """Starts or stops the metronome."""
    if self.is_running:
      Clock.unschedule(self.tick)
      self.is_running = False
      self.beat_count = 0
    else:
      Clock.schedule_interval(self.tick, 60.0 / self.bpm)
      self.is_running = True

  def tick(self, dt: float) -> None:
    """Executes the metronome beat."""
    if self.beat_count == 0:
      print("Playing click1")
      # self.sound_manager.play_click1()
      if click1:
        click1.play()
    else:
      print("Playing click2")
      # self.sound_manager.play_click2()
      if click2:
        click2.play()

    self.beat_count = (self.beat_count + 1) % self.beats_per_measure