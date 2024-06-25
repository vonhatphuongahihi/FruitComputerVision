import pygame
import sys
from settings import *
from background import Background
import ui
import image
class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background('assets/images/menu_bg.jpg')
        self.click_sound_start = pygame.mixer.Sound(f"assets/sounds/GameStart.wav")
        self.click_sound_quit = pygame.mixer.Sound(f"assets/sounds/MainMenuExit.wav")
    def draw(self):
        self.background.draw(self.surface)
    def update(self):
        self.draw()
        if ui.button(self.surface, 320, "Start", click_sound=self.click_sound_start):
            return "game"
        if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "Quit", click_sound=self.click_sound_quit):
            pygame.quit()
            sys.exit()
