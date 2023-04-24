import pygame
import os
from src.config import *

pygame.init()

def draw_picture(img_background, draw_background , text = 0, color_text = 0, font = 0, coord_center_x = 0, coord_center_y = 0):
    if (draw_background):
        screen.blit(img_background, (0, 0))
    if (text != 0):
        text = font.render(text, False, color_text)
        text_rect = text.get_rect(center=(coord_center_x, coord_center_y))
        screen.blit(text, text_rect)

