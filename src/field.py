import pygame
from src.config import *
from src.ship import Ship
from src.button_on_field import *

pygame.init()

class Field():
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.size = 40
        self.cnt = 10
        self.button = list()
        self.ships = list()
        for x in range(self.cnt):
            self.button.append(list())
            for y in range(self.cnt):
                button = ButtonField(self.rect.x + self.size * (x + 1), self.rect.y + self.size * (y + 1), self.size, self.size)
                self.button[x].append(button)
    def draw(self):
        for x in range(self.cnt + 1):
            for y in range(self.cnt + 1):
                coord = pygame.Rect(self.rect.x + self.size * x, self.rect.y + self.size * y, self.size, self.size)
                if (y == 0 and x == 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                if (y == 0 and x != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    letter = chr(ord('A') + x - 1)
                    text1 = letter_font.render(f'{letter}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + self.size * x + self.size / 3, self.rect.y + self.size * y + self.size / 4))
                elif (x == 0 and y != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    text1 = letter_font.render(f'{y}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + self.size * x + self.size / 3, self.rect.y + self.size * y + self.size / 4))
                else:
                    self.button[x - 1][y - 1].draw()
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
    def update(self, block, NUMBER_TURN):
        if (not block):
            for x in range(self.cnt):
                for y in range(self.cnt):
                    self.button[x][y].update(block, NUMBER_TURN)
    def clear(self):
        for x in range(self.cnt):
            for y in range(self.cnt):
                self.button[x][y].clear()
    
    def check(self):
        check_history = [[self.button[i][j].flag for j in range(0, self.cnt)] for i in range(0, self.cnt)]
        self.ships = list()
        cnt_list = [4, 3, 2, 1]
        
        for coord in range(0, self.cnt): 
            y, x = 0, coord
            while y < self.cnt:
                cnt = 0
                start = y
                while(y < self.cnt and self.button[x][y].flag == 1 and check_history[x][y] != -1):
                    cnt += 1
                    y += 1
                if (cnt > 4):
                    return False
                if (cnt > 0 and check_area(self, x, start, x, y - 1)):
                    cnt_list[cnt - 1] -= 1
                    list_button = []
                    for i in range (0, cnt):
                        check_history[x][start + i] = -1
                        list_button.append(self.button[x][start + i])
                    self.ships.append(Ship(list_button, x, start, x, y - 1))
                y += 1
            x, y = 0, coord
            while x < self.cnt:
                cnt = 0
                start = x
                while(x < self.cnt and self.button[x][y].flag == 1 and check_history[x][y] != -1):
                    cnt += 1
                    x += 1
                if (cnt > 4):
                    return False
                if (cnt > 0 and check_area(self, start, y, x - 1, y)):
                    cnt_list[cnt - 1] -= 1
                    list_button = []
                    for i in range (0, cnt):
                        check_history[start + i][y] = -1
                        list_button.append(self.button[start + i][y])
                    self.ships.append(Ship(list_button, start, y, x - 1, y))
                x += 1
        
        for i in range(0, 4):
            if (cnt_list[i] != 0):
                return False
        for i in range(0, self.cnt):
            for j in range(0, self.cnt):
                if (check_history[i][j] == 1):
                    return False
        return True

def check_area(field, x1, y1, x2, y2):
    for x in range(max(0, x1 - 1), min(field.cnt, x2 + 2)):
        for y in range(max(0, y1 - 1), min(field.cnt, y2 + 2)):
            if (not (x1 <= x and x <= x2 and y1 <= y and y <= y2)) and field.button[x][y].flag == 1:
                return False
    return True