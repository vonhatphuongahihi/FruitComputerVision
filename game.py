import pygame
import random
import time
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background('assets/images/background.png')
        self.cap = cv2.VideoCapture(0)
        self.sounds = {}
        self.sounds["im_out"] = pygame.mixer.Sound("assets/sounds/LoseLife.wav")
        self.reset()

    def reset(self):
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.fruits = []
        self.spawn_fruits()
        self.score = 0
        self.game_start_time = time.time()
        self.time_left = GAME_DURATION

    def spawn_fruits(self):
        for fruit in ['melon', 'orange', 'pomegranate', 'guava', 'bomb']:
            self.generate_random_fruits(fruit)

    def generate_random_fruits(self, fruit):
        fruit_path = f"assets/images/{fruit}.png"
        data = {
            'img': pygame.image.load(fruit_path),
            'x': random.randint(100, 500),
            'y': 800,
            'speed_x': random.randint(-10, 10),
            'speed_y': random.randint(-80, -60),
            'throw': random.random() >= 0.75,
            't': 0,
            'hit': False
        }
        self.fruits.append(data)

    def load_camera(self):
        _, self.frame = self.cap.read()

    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.follow_mediapipe_hand(x, y)

    def draw(self):
        self.background.draw(self.surface)
        for fruit in self.fruits:
            if fruit['throw']:
                self.surface.blit(fruit['img'], (fruit['x'], fruit['y']))
        self.hand.draw(self.surface)
        ui.draw_text(self.surface, f"Score: {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"], shadow=False)
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"]
        ui.draw_text(self.surface, f"Time left: {self.time_left}", (SCREEN_WIDTH//2, 5), timer_text_color, font=FONTS["medium"], shadow=False)

    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)

    def update(self):
        self.load_camera()
        self.set_hand_position()
        self.game_time_update()
        self.draw()
        if self.time_left > 0:
            self.update_fruits()
        else:
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["im_out"]):
                return "menu"
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def update_fruits(self):
        for fruit in self.fruits:
            if fruit['throw']:
                fruit['x'] += fruit['speed_x']
                fruit['y'] += fruit['speed_y']
                fruit['speed_y'] += (1 * fruit['t'])
                fruit['t'] += 1
                if fruit['y'] > SCREEN_HEIGHT or fruit['x'] > SCREEN_WIDTH or fruit['x'] < 0:
                    self.generate_random_fruits(fruit)
                if self.hand.rect.collidepoint((fruit['x'], fruit['y'])) and not fruit['hit']:
                    if fruit['img'] == 'assets/images/bomb.png':
                        self.time_left -= 5
                    else:
                        self.score += 1
                    fruit['hit'] = True

        self.fruits = [fruit for fruit in self.fruits if not fruit['hit']]

