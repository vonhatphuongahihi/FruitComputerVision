import pygame
WINDOW_NAME = "Fruit Ninja -- Phuong"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH, SCREEN_HEIGHT = 880, 750
FPS = 12
DRAW_FPS = True
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 180
HAND_HITBOX_SIZE = (60, 80)
FRUIT_SIZES = (80,80)
FRUIT_SIZE_RANDOMIZE = (1,2)
BOMB_SIZES = (100, 100)
BOMB_SIZE_RANDOMIZE = (1.2,1.5)
FRUIT_SPAWN_TIME = 1
FRUIT_MOVE_SPEED = {"min": 1, "max": 6}
ANIMATION_SPEED = 0.1
GAME_DURATION = 60
DRAW_HITBOX = False
MUSIC_VOLUME = 0.5
SOUNDS_VOLUME = 0.2
COLORS = {"title": (255, 255, 255), "score": (255, 255, 255), "timer": (255, 255, 255),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (0, 0, 0)}}
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font("assets/GangOfThree.ttf", 36)
FONTS["medium"] = pygame.font.Font("assets/GangOfThree.ttf", 50)
FONTS["big"] = pygame.font.Font("assets/GangOfThree.ttf", 120)
