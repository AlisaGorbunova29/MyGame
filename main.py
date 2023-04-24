import pygame
from src.game_play import *

pygame.init()   
     
play = True
while (play):
    play = game_play()
pygame.quit()