import pygame
import os
from config import game_folder, WIDTH, HEIGHT

pygame.init()

CARD_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'card.png')).convert()
CARD_IMG = pygame.transform.scale(CARD_IMG, (WIDTH, HEIGHT))

BACKGROUND_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'background.png')).convert()
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

WATER_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'water.png')).convert()
WATER_IMG = pygame.transform.scale(WATER_IMG, (50, 50))

SHIP_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'ship_img.png')).convert()
SHIP_IMG = pygame.transform.scale(SHIP_IMG, (50, 50))

HIT_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'hit.png')).convert()
HIT_IMG = pygame.transform.scale(HIT_IMG, (WIDTH, HEIGHT))

PAST_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'past.png')).convert()
PAST_IMG = pygame.transform.scale(PAST_IMG, (WIDTH, HEIGHT))

STAGE_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'card.png')).convert()
STAGE_IMG = pygame.transform.scale(STAGE_IMG, (WIDTH, HEIGHT))

