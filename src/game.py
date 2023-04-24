import pygame
import time
from src.img import *
from src.player import *
from src.button import *
from src.config import *
from src.robot import *

pygame.init()

class Game():
    def __init__(self):
        #игроки
        self.player = [Player(50, 100, 440, 440), Player(550, 100, 440, 440)]
        self.robot = Robot(550, 100, 440, 440)
        
        #параметры игры
        self.number_turn = 0   # номер хода
        self.stage = "start"    # этап игры
        self.block = False      # есть ли блокировка полей
        self.with_robot = False # игра с роботом
        self.now_play = 1       # номер игрока который сейчас играет
        self.play = 0           # 0 - игра идет, -1 = окончание игры и запуск заново, -2 = окончание игры совсем
        self.hit_now = False    # попал ли игрок на прошлом ходу
        self.kill_now = False   # потопил ли игро на прошлом ходу 
    
    def update(self):
        self.player[0].update(self.block, self.number_turn)
        self.player[1].update(self.block, self.number_turn)
        button_confirm.update(self.block)
        button_yes.update(self.block)
        button_no.update(self.block)
        button_no_robot.update(self.block)
        button_with_robot.update(self.block)

    def change_stage(self, first, second):
        self.player[self.now_play].change_stage(first)
        self.player[(self.now_play + 1) % 2].change_stage(second)

    def draw_player_field(self):
        if (self.with_robot):
            self.player[0].draw(1)
            self.player[1].draw('robot')
        else:
            self.player[0].draw(1)
            self.player[1].draw(2)

    def start(self):
        # обновления
        self.block = False
        self.update()

        #отрисовка
        draw_picture(CARD_IMG, True, 'Игра "Морской бой"', BLACK, title, WIDTH / 2 + 25, HEIGHT /2 - 50)
        draw_button(False, False, False, True, True)
        pygame.display.flip()

        if (button_with_robot.is_click):
            self.with_robot = True
            self.player[1] = self.robot

    def robot_placement(self):
        self.robot.placement_of_ships()
        self.robot.field.check()

    def placement_of_ships(self):
        self.block = False
        self.change_stage(1, 2)
        self.update()
        
        #отрисовка
        draw_picture(BACKGROUND_IMG, True)
        draw_button(True, False, False, False, False)
        self.draw_player_field()

        pygame.display.flip()

        
    def repeat(self):
        self.change_stage(2, 2)
        self.update()
        self.block = True
        button_confirm.is_click = False
        
        draw_picture(STAGE_IMG, True, 'НЕКОРРЕКТНЫЙ ВВОД', BLACK, subtitle, WIDTH / 2, HEIGHT /2 - 100)
        draw_picture(STAGE_IMG, False, 'ПОПРОБУЙТЕ ЕЩЁ РАЗ', BLACK, subtitle, WIDTH / 2, HEIGHT /2)

        pygame.display.flip()

        time.sleep(2)

    def pause(self):
        #обновления
        self.number_turn += 1
        self.change_stage(2, 2)
        self.update()
        self.now_play = (self.now_play + 1) % 2
        self.block = True
        button_confirm.is_click = False
        
        #отрисовка
        if (self.stage == "before game"):
            draw_picture(STAGE_IMG, True, 'ИГРА НАЧАЛАСЬ!', BLACK, title, WIDTH / 2, HEIGHT /2)
        elif (self.stage == "before placement" and self.with_robot):
            draw_picture(STAGE_IMG, True, 'РАССТАНОВКА КОРАБЛЕЙ НА ПОЛЕ', BLACK, subtitle, WIDTH / 2, HEIGHT /2)
        else:
            draw_picture(STAGE_IMG, True, f'ИГРОК {self.now_play + 1}', BLACK, subtitle, WIDTH / 2, HEIGHT /2 - 100)
            draw_picture(STAGE_IMG, False, 'РАССТАНОВКА КОРАБЛЕЙ НА ПОЛЕ', BLACK, subtitle, WIDTH / 2, HEIGHT /2)

        pygame.display.flip()
        time.sleep(2)

    def move(self):
        self.block = False
        if (self.with_robot and self.now_play == 1):
            self.change_stage(2, 2)
            self.robot.our_move(self.player[0].field, self.number_turn)
        else:
            self.change_stage(2, 3)
        self.update()

        #Отрисовка
        screen.blit(BACKGROUND_IMG, (0, 0))
        self.draw_player_field()
        draw_button(True, False, False, False, False)

        #Переворачивание экрана
        pygame.display.flip()
        if (self.with_robot and self.now_play == 1):
            time.sleep(1)
         
        #Анализ      
        i = self.now_play
        enemy = (i + 1) % 2
        if (self.player[enemy].hit):
            self.hit_now = True
        if (self.player[enemy].kill):
            self.kill_now = True
            
    def analisis(self):
        self.number_turn += 1
        self.change_stage(2, 2)
        self.update()
        self.block = True
        self.player[0].clear()
        self.player[1].clear()
        
        if(self.kill_now):
            draw_picture(HIT_IMG, True, 'УТОПИЛ!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            BATTLE_SOUND.play()
        elif (self.hit_now):
            draw_picture(HIT_IMG, True, 'ПОПАЛ!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            BATTLE_SOUND.play()
        else:
            draw_picture(PAST_IMG, True, 'МИМО!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            WATER_SOUND.play()

        pygame.display.flip()
        time.sleep(2.7)
        
        if (not self.hit_now):
            self.now_play = (self.now_play + 1) % 2
        self.number_turn += 1
        self.hit_now = False
        self.kill_now = False

    def end(self):
        self.block = False
        button_no.is_click = False
        button_yes.is_click = False
        self.update()
        
        draw_picture(CARD_IMG, True, 'Победил робот', BLACK, title, WIDTH / 2, HEIGHT /2)
        if (self.with_robot and self.now_play % 2 + 1 == 2):
            draw_picture(CARD_IMG, True, 'Победил робот', BLACK, title, WIDTH / 2, HEIGHT /2)
        elif (self.with_robot and self.now_play % 2 + 1 == 1):
            draw_picture(CARD_IMG, True, 'Победил игрок', BLACK, title, WIDTH / 2, HEIGHT /2)
        else:
            draw_picture(CARD_IMG, True, f'Победил игрок {self.now_play % 2 + 1}', BLACK, title, WIDTH / 2, HEIGHT /2)
        draw_picture(CARD_IMG, False, f'Хотите сыграть ещё раз?', BLACK, subtitle, WIDTH / 2, HEIGHT /2 + 200)
        draw_button(False, True, True, False, False)
        
        pygame.display.flip()

        if (button_yes.is_click):
                self.play = -1
        if (button_no.is_click):
                self.play = -2