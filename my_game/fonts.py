import pygame
import os
from config import game_folder

pygame.init()

#шрифты
main = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 32)
text_button = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 40)
title = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 80)
subtitle = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 60)
big = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 120)