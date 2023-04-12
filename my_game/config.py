import pygame
import os

pygame.init()

# размеры поля
WIDTH = 1050
HEIGHT = 800
FPS = 30

#этап игры
NUMBER_TURNE = 0  

print(NUMBER_TURNE)

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

