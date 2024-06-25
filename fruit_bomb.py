import pygame
import random
from settings import *

class FruitBase:
    def __init__(self, name, img_path, x_range, y_start, speed_x_range, speed_y_range):
        self.name = name
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()  # Thêm dòng này để tạo thuộc tính rect
        self.x = random.randint(x_range[0], x_range[1])
        self.y = y_start
        self.speed_x = random.randint(speed_x_range[0], speed_x_range[1])
        self.speed_y = random.randint(speed_y_range[0], speed_y_range[1])
        self.throw = random.random() >= 0.75
        self.t = 0
        self.hit = False

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.topleft = (self.x, self.y)  # Cập nhật vị trí của rect
        self.speed_y += 1 * self.t
        self.t += 1

    def draw(self, window):
        if self.throw and self.y <= SCREEN_HEIGHT:
            window.blit(self.image, (self.x, self.y))
        else:
            self.reset()

    def reset(self):
        self.x = random.randint(100, 1000)
        self.y = SCREEN_HEIGHT
        self.rect.topleft = (self.x, self.y)  # Cập nhật vị trí của rect khi reset
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-80, -60)
        self.throw = random.random() >= 0.75
        self.t = 0
        self.hit = False
        self.image = pygame.image.load(f"assets/images/{self.name}.png")



class Fruit(FruitBase):
    def __init__(self, name):
        img_path = f"assets/images/{name}.png"
        super().__init__(name, img_path, (100, 1000), 750, (-10, 10), (-80, -60))



    def kill(self, rms):
        half_fruit_path = f"assets/images/half_{self.name}.png"
        self.image = pygame.image.load(half_fruit_path)
        self.speed_x += 10
        return 1

class Bomb(FruitBase):
    def __init__(self):
        img_path = "assets/images/bomb.png"
        super().__init__("bomb", img_path, (100, 1000), 750, (-10, 10), (-80, -60))



    def kill(self, rms):
        self.image = pygame.image.load("assets/images/explosion.png")
        return -10