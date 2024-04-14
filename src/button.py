import pygame
from src.config import *

pygame.init()

#класс для всех базовых кнопок
class ButtonBasic():
    def __init__(self,x, y, width, height, messege):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.is_click = False
        self.is_block = False
        self.messege = messege
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text1 = text_button.render(f'{self.messege}', False, BLACK)
        text_rect = text1.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))
        screen.blit(text1, text_rect)
    def update(self):
        if (not self.is_block):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (self.rect.collidepoint(mouse[0], mouse[1]) and click[0]):
                self.is_click = True
    def refresh(self, block):
        self.is_click = False
        self.is_block = block

class ButtonVariant():
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.is_click = False
        self.is_block = False
        self.messege = ""
        self.flag = False
        self.color = WHITE
    def draw(self, messege = [], flag = [], show = False):
        self.messege = messege
        self.flag = flag
        mouse = pygame.mouse.get_pos()
        if (self.is_click):
            if (self.flag):
                self.color = GREEN
            else:
                self.color = RED
        elif (self.rect.collidepoint(mouse[0], mouse[1])):
            self.color = LIGHTYELLOW
        else:
            self.color = WHITE

        if (show and flag):
            self.color = GREEN

        pygame.draw.rect(screen, self.color, self.rect)        
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text1 = text_button.render(f'{self.messege}', False, BLACK)
        text_rect = text1.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))
        screen.blit(text1, text_rect)
    def update(self):
        if (not self.is_block):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (self.rect.collidepoint(mouse[0], mouse[1]) and click[0]):
                self.is_click = True
    def refresh(self, block):
        self.is_click = False
        self.is_block = block

class Button():
    def __init__(self):
        self.button = { 'with_robot': ButtonBasic(150, 450, 350, 75, 'Игра с роботом'),
                        'no_robot': ButtonBasic(600, 450, 350, 75, 'Игра без робота'),
                        'confirm': ButtonBasic(350, 650, 350, 75, 'Подвердить ввод'), 
                        'first_variant': ButtonVariant(150, 250, 350, 75),
                        'second_variant': ButtonVariant(600, 250, 350, 75),
                        'third_variant': ButtonVariant(150, 450, 350, 75),
                        'forth_variant': ButtonVariant(600, 450, 350, 75),
                        'yes': ButtonBasic(150, 650, 350, 75, 'ДА'),
                        'no': ButtonBasic(600, 650, 350, 75, 'НЕТ')}
    def refresh(self, block):
        number = 0
        for i in self.button.values():
            i.refresh(block[number])
            number += 1
    def draw(self, draw, messege=[], flag=[]):
        number = 0
        show = False
        if (self.button['first_variant'].is_click or self.button['second_variant'].is_click or self.button['third_variant'].is_click or self.button['forth_variant'].is_click):
            show = True
        for i in self.button.values():
            if (draw[number]):
                if (number < 3 or number > 6):
                    i.draw()
                else:
                    i.draw(messege[number - 3], flag[number - 3], show)
            number += 1
    def update(self):
        for i in self.button.values():
            i.update()

our_buttons = Button()