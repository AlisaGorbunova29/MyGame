import pygame
from config import *
from fonts import text_button

pygame.init()


class ButtonStart():
    def __init__(self,x, y, width, height, messege):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.is_click = False
        self.messege = messege
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text1 = text_button.render(f'{self.messege}', False, BLACK)
        text_rect = text1.get_rect(center=(self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))
        screen.blit(text1, text_rect)
    def update(self, block):
        if (not block):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (self.rect.collidepoint(mouse[0], mouse[1]) and click[0]):
                self.is_click = True