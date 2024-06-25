import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2
import random
class Hand:
    def __init__(self):
        self.orig_image = image.load("assets/images/phi_tieu.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("assets/images/phi_tieu.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False
    def follow_mouse(self):
        self.rect.center = pygame.mouse.get_pos()
    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)
    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)
    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)
    def on_rm(self, rms):
        return [rm for rm in rms if self.rect.colliderect(rm.rect)]
    def kill_rms(self, rms, score, sounds):
        bombSounds ='assets/sounds/BombExplode.wav'
        if self.left_click:
            for rm in self.on_rm(rms):
                bombSound = bombSounds
                rm_score = rm.kill(rms)
                score += rm_score
                if rm_score < 0:
                    pygame.mixer.Sound(bombSound).play().set_volume(SOUNDS_VOLUME)
                else:
                    pygame.mixer.Sound('assets/sounds/FruitSlice.wav').play().set_volume(SOUNDS_VOLUME)
        else:
            self.left_click = False
        return score
