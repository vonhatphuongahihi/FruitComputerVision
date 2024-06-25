import pygame
WINDOW_NAME = "Fruit Ninja -- Phuong"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 750
FPS = 12
DRAW_FPS = True
# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 180
HAND_HITBOX_SIZE = (60, 80)
# drawing
DRAW_HITBOX = False # will draw all the hitbox
# animation
ANIMATION_SPEED = 0.09 # the frame of the deities will change every X sec
# difficulty
GAME_DURATION = 90 # the game will last X sec
# colors
COLORS = {"title": (255, 255, 255), "score": (255, 255, 255), "timer": (255, 255, 255),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (0, 0, 0)}} # second is the color when the mouse is on the button
# sounds / music
MUSIC_VOLUME = 0.5 
SOUNDS_VOLUME = 0.2
# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
