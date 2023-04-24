import pygame
from src.config import WIDTH, HEIGHT
import os

pygame.init()

#путь к файлам
game_folder = os.path.dirname(__file__)

#Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Морской бой")
clock = pygame.time.Clock()