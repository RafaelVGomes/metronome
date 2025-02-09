from kivy.core.audio import SoundLoader
from pathlib import Path

# Define the base directory and the path to the sounds
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# SOUNDS_DIR = BASE_DIR / "assets" / "sounds"

class SoundManager:
  def __init__(self):
    self.click1 = None
    self.click2 = None
    self.load_sounds()

  def load_sounds(self) -> None:
    """Loads the sounds on initialization."""

    self.click1 = SoundLoader.load('assets/sounds/click1.wav')
    self.click2 = SoundLoader.load('assets/sounds/click2.wav')

    # click1_path = SOUNDS_DIR / "click1.wav"
    # click2_path = SOUNDS_DIR / "click2.wav"
    
    # if click1_path.exists():
    #     self.click1 = SoundLoader.load(str(click1_path))
    #     if self.click1:
    #         print(f"Loaded sound: {click1_path}")
    #     else:
    #         print(f"Failed to load sound: {click1_path}")
    # else:
    #     print(f"Warning: {click1_path} not found.")
    
    # if click2_path.exists():
    #     self.click2 = SoundLoader.load(str(click2_path))
    #     if self.click2:
    #         print(f"Loaded sound: {click2_path}")
    #     else:
    #         print(f"Failed to load sound: {click2_path}")
    # else:
    #     print(f"Warning: {click2_path} not found.")

  def play_click1(self) -> None:
    """Toca o som click1."""
    if self.click1:
      print("Playing click1 sound")
      self.click1.play()
    else:
      print("Warning: click1 sound not loaded.")

  def play_click2(self) -> None:
    """Toca o som click2."""
    if self.click2:
      print("Playing click2 sound")
      self.click2.play()
    else:
      print("Warning: click2 sound not loaded.")

