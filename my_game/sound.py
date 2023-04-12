import pygame
import os
from config import game_folder

pygame.init()

BACKGROUND_SOUND = pygame.mixer.music.load(os.path.join(game_folder, 'music', 'background_sound.mp3'))
pygame.mixer.music.set_volume(0.2)
WATER_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'water_sound.wav'))
BATTLE_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'battle.wav'))
