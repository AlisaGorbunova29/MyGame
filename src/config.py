import pygame
import os

pygame.init()

# размеры поля
WIDTH = 1050
HEIGHT = 800
FPS = 30

# цвета
MIDNIGTHBLUE = (25, 25, 112)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
LIGHTBLUE = (0, 206, 209 )
LIGHTYELLOW = (255, 255, 224)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
LIGHTCORAL = (240, 128, 128)
RED = (255, 0, 0)
CORNSILK = (255, 248, 220)

#путь к файлам
game_folder = os.path.dirname(__file__)

#экран и время
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Морской бой")

clock = pygame.time.Clock()

#шрифты
main = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 32)
letter_font = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 26)
text_button = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 40)
title = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 80)
subtitle = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 60)
big = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 120)

# изображения
CARD_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'card.png')).convert()
CARD_IMG = pygame.transform.scale(CARD_IMG, (WIDTH, HEIGHT))

BACKGROUND_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'background.png')).convert()
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

WATER_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'water.png')).convert()
WATER_IMG = pygame.transform.scale(WATER_IMG, (40, 40))

SHIP_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'ship_img.png')).convert()
SHIP_IMG = pygame.transform.scale(SHIP_IMG, (40, 40))

HIT_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'hit.png')).convert()
HIT_IMG = pygame.transform.scale(HIT_IMG, (WIDTH, HEIGHT))

PAST_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'past.png')).convert()
PAST_IMG = pygame.transform.scale(PAST_IMG, (WIDTH, HEIGHT))

STAGE_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'card.png')).convert()
STAGE_IMG = pygame.transform.scale(STAGE_IMG, (WIDTH, HEIGHT))

#звуки
pygame.mixer.init()

BACKGROUND_SOUND = pygame.mixer.music.load(os.path.join(game_folder, 'music', 'background_sound.mp3'))
pygame.mixer.music.set_volume(0.2)
WATER_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'water_sound.wav'))
BATTLE_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'battle.wav'))

