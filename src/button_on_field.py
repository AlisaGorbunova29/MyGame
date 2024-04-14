import pygame
from src.config import *
from src.img import *

pygame.init()

class ButtonField():
    def __init__(self,x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.flag = 0
        self.color = WHITE
        self.change = 0
        self.stage = 2 #1 - расстановка,  2 - блокировка, 3 - бой
    def clear(self):
        self.flag = 0
        self.color = WHITE
        self.change = 0
    def draw(self):
        mouse = pygame.mouse.get_pos()
        if (self.rect.collidepoint(mouse[0], mouse[1]) and self.stage != 2 and self.color == WHITE):
            pygame.draw.rect(screen, LIGHTYELLOW, self.rect)
        else:
            if (self.color == LIGHTBLUE):
                screen.blit(WATER_IMG, (self.rect.x, self.rect.y))
            elif (self.color == BLACK):
                screen.blit(SHIP_IMG, (self.rect.x, self.rect.y))
            else:
                pygame.draw.rect(screen, self.color, self.rect)
    def update(self, block, NUMBER_TURN):
        if (not block):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (self.stage == 2 and self.color == YELLOW):
                self.color = WHITE
            elif (self.rect.collidepoint(mouse[0], mouse[1]) and click[0] and self.change == 0):
                if (self.stage == 1):
                    self.flag = 1
                    self.color = YELLOW
                if (self.stage == 3):
                    if (self.flag == 0):
                        self.color = LIGHTBLUE
                        self.change = NUMBER_TURN
                    else:
                        self.color = BLACK
                        self.change = -NUMBER_TURN

