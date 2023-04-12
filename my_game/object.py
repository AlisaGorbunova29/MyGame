import pygame
from config import *
from img import *
from fonts import *

pygame.init()

class Button():
    def __init__(self,x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.flag = 0
        self.color = WHITE
        self.change = 0
        self.stage = 1
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
    def update(self, block, NUMBER_TURNE):
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
                        self.change = NUMBER_TURNE
                    else:
                        self.color = BLACK
                        self.change = -NUMBER_TURNE


class Field():
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        size = 50
        self.ships = list()
        for x in range(8):
            self.ships.append(list())
            for y in range(8):
                ship = Button(self.rect.x + size * (x + 1), self.rect.y + size * (y + 1), size, size)
                self.ships[x].append(ship)
    def draw(self):
        size = 50
        for x in range(9):
            for y in range(9):
                coord = pygame.Rect(self.rect.x + size * x, self.rect.y + size * y, size, size)
                if (y == 0 and x == 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                if (y == 0 and x != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    letter = chr(ord('A') + x - 1)
                    text1 = main.render(f'{letter}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + size * x + size / 3, self.rect.y + size * y + size / 4))
                elif (x == 0 and y != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    text1 = main.render(f'{y}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + size * x + size / 3, self.rect.y + size * y + size / 4))
                else:
                    self.ships[x - 1][y - 1].draw()
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
    def update(self, block, NUMBER_TURNE):
        if (not block):
            for x in range(8):
                for y in range(8):
                    self.ships[x][y].update(block, NUMBER_TURNE)  


class Player():
    def __init__(self, x, y, width, height):
        self.field = Field(x, y, width, height)
        self.cnt_ships = 0
        self.stage = 1
        self.hit = False
        self.change = False
    def update(self, block, NUMBER_TURNE):
        if (not block):
            self.field.update(block, NUMBER_TURNE)
            self.change = False
            self.hit = False
            self.cnt_ships = 0
            for x in range(8):
                for y in range(8):
                    if (self.field.ships[x][y].change == NUMBER_TURNE and self.field.ships[x][y].stage == 3):
                        self.change = True
                    if (self.field.ships[x][y].change == -NUMBER_TURNE and self.field.ships[x][y].stage == 3):
                        self.change = True
                        self.hit = True
                        self.field.ships[x][y].flag = -1
                    if (self.field.ships[x][y].flag == 1):
                        self.cnt_ships += 1
    def change_stage(self, new_stage):
        self.stage = new_stage
        for x in range(8):
            for y in range(8):
                self.field.ships[x][y].stage = self.stage
    def draw(self, number):
        self.field.draw()
        text = main.render(f'Поле игрока {number}', False, (0, 0, 0))
        text_rect = text.get_rect(center=(self.field.rect.x  + self.field.rect.width / 2, self.field.rect.y - 50))
        screen.blit(text, text_rect)
