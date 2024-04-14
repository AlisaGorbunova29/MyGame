import pygame
from src.config import *
from src.img import *
from src.ship import Ship
from src.field import *

pygame.init()

class Player():
    def __init__(self, x, y, width, height):
        self.field = Field(x, y, width, height)
        self.cnt_ships = 0
        self.stage = 1
        self.hit = False
        self.change = False
        self.kill = False
    def update(self, block, NUMBER_TURN):
        if (not block):
            self.field.update(block, NUMBER_TURN)
            self.change = False
            self.hit = False
            self.kill = False
            self.cnt_ships = 0
            for i in self.field.ships:
                for j in i.list_ship:
                    if (j.change == -NUMBER_TURN and j.stage > 1):
                        self.change = True
                        self.hit = True
                        j.flag = -1
                        if (i.cnt_alive == 1):
                            self.kill = True
                            self.open_area(i.head_x, i.head_y, i.tail_x, i.tail_y, NUMBER_TURN)
                        i.cnt_alive -= 1
            for x in range(self.field.cnt):
                for y in range(self.field.cnt):
                    if (self.field.button[x][y].change == NUMBER_TURN and self.field.button[x][y].stage > 1):
                        self.change = True
                    if (self.field.button[x][y].flag == 1):
                        self.cnt_ships += 1
    def change_stage(self, new_stage):
        self.stage = new_stage
        for x in range(self.field.cnt):
            for y in range(self.field.cnt):
                self.field.button[x][y].stage = self.stage
    def draw(self, number):
        self.field.draw()
        text = main.render(f'Player {number} field', False, (0, 0, 0))
        text_rect = text.get_rect(center=(self.field.rect.x  + self.field.rect.width / 2, self.field.rect.y - 50))
        screen.blit(text, text_rect)
    def clear(self):
        self.change = False
        self.hit = False
    def open_area(self, x1, y1, x2, y2, NUMBER_TURN):
        for x in range(max(0, x1 - 1), min(self.field.cnt, x2 + 2)):
            for y in range(max(0, y1 - 1), min(self.field.cnt, y2 + 2)):
                if (self.field.button[x][y].flag == 0):
                    self.field.button[x][y].color = LIGHTBLUE
                    self.field.button[x][y].change = NUMBER_TURN
                else:
                    self.field.button[x][y].color = BLACK
                    self.field.button[x][y].change = -NUMBER_TURN
