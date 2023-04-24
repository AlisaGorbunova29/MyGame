import pygame
from src.config import *

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

#кнопки
button_confirm = ButtonStart(350, 650, 350, 75, 'Подвердить ввод')
button_yes = ButtonStart(150, 650, 350, 75, 'ДА')
button_no = ButtonStart(600, 650, 350, 75, 'НЕТ')
button_with_robot = ButtonStart(150, 450, 350, 75, 'Игра с роботом')
button_no_robot = ButtonStart(600, 450, 350, 75, 'Игра без робота')

def draw_button(confirm_draw, yes_draw, no_draw, with_robot_draw, no_robot_draw):
    if confirm_draw:
        button_confirm.draw()
    if yes_draw:
        button_yes.draw()
    if no_draw:
        button_no.draw()
    if with_robot_draw:
        button_with_robot.draw()
    if no_robot_draw:
        button_no_robot.draw()

def refresh():
    button_confirm.is_click = False
    button_yes.is_click = False
    button_no.is_click = False
    button_with_robot.is_click = False
    button_no_robot.is_click = False