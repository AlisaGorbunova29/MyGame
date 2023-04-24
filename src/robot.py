import pygame
import random
import src.config as config
from src.player import Player

pygame.init()

class Robot(Player):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.cnt_box = 10
        self.ship_map = [[0 for j in range(0, self.cnt_box)] for i in range (0, self.cnt_box)]
    def placement_of_ships(self):
        for type in range (3, -1, -1):
            for cnt_ship in range (4 - type):
                flag = True
                box = list(range(0, (self.cnt_box - type) * (self.cnt_box - type)))
                random.shuffle(box)
                for number in box:
                    head = ((number // (self.cnt_box - type)), (number % (self.cnt_box - type)))
                    side = random.randint(0, 1)
                    if (side):
                        tail = [head[0], head[1] + type]
                    else:
                        tail = [head[0] + type, head[1]]
                    flag = False
                    for x in range(max(0, head[0] - 1), min(self.cnt_box, tail[0] + 2)):
                        for y in range(max(0, head[1] - 1), min(self.cnt_box, tail[1] + 2)):
                            if (self.ship_map[x][y] == 1):
                                flag = True
                    if (not flag):
                        break
                for x in range(head[0], tail[0] + 1):
                    for y in range(head[1], tail[1] + 1):
                        self.ship_map[x][y] = 1
                        self.field.button[x][y].flag = 1

    def our_move(self, field, NUMBER_TURN):
        flag = True
        while (flag):
            (x, y) = (random.randint(0, self.cnt_box - 1), random.randint(0, self.cnt_box - 1))
            flag = False
            if (field.button[x][y].change != 0):
                flag = True
        if (field.button[x][y].flag == 0):
            field.button[x][y].color = config.LIGHTBLUE
            field.button[x][y].change = NUMBER_TURN
        else:
            field.button[x][y].color = config.BLACK
            field.button[x][y].change = -NUMBER_TURN