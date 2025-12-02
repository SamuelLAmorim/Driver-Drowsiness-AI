import pygame
import os

class AlertSystem:
    def __init__(self):
        pygame.mixer.init()
        self.sound_path = os.path.join("assets", "alarm.wav")

    def play(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.sound_path)
            pygame.mixer.music.play(-1)  # loop

    def stop(self):
        pygame.mixer.music.stop()