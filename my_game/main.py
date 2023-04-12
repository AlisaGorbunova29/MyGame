import pygame
from play_game import game_play



#Создаем игру и окно
pygame.init()   
     
play = True
while (play):
    play = game_play()
pygame.quit()