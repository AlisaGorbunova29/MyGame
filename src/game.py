import pygame
import time
import random
from src.img import *
from src.player import *
from src.button import *
from src.config import *
from src.robot import *
from src.question import *

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
        self.info_question = [] #информация о вопросе
    
    def update(self):
        our_buttons.update()
        self.player[0].update(self.block, self.number_turn)
        self.player[1].update(self.block, self.number_turn)
       
    
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
        self.change_stage(2, 2)
        self.update()

        #отрисовка
        draw_picture(CARD_IMG, True, 'Naval Quiz"', BLACK, title, WIDTH / 2 + 25, HEIGHT /2 - 50)
        our_buttons.draw([True, True, False, False, False, False, False, False, False])
        pygame.display.flip()

        if (our_buttons.button['with_robot'].is_click):
            self.with_robot = True
            self.player[1] = self.robot

    def robot_placement(self):
        self.robot.placement_of_ships()
        self.robot.field.check()

    def placement_of_ships(self):
        self.block = False
        self.update()
        self.change_stage(1, 2)
        
        
        #отрисовка
        draw_picture(BACKGROUND_IMG, True)
        our_buttons.draw([False, False, True, False, False, False, False, False, False])
        self.draw_player_field()

        pygame.display.flip()

        
    def repeat(self):
        self.change_stage(2, 2)
        self.block = True
        self.update()
        
        draw_picture(STAGE_IMG, True, 'INCORRECT INPUT', BLACK, subtitle, WIDTH / 2, HEIGHT /2 - 100)
        draw_picture(STAGE_IMG, False, 'TRY AGAIN', BLACK, subtitle, WIDTH / 2, HEIGHT /2)

        pygame.display.flip()

        time.sleep(SLEEP_TIME)

    def pause(self):
        #обновления
        self.number_turn += 1
        self.change_stage(2, 2)
        self.now_play = (self.now_play + 1) % 2
        self.update()
        self.block = True
        
        
        #отрисовка
        if (self.stage == "before game"):
            draw_picture(STAGE_IMG, True, 'START!', BLACK, title, WIDTH / 2, HEIGHT /2)
        elif (self.stage == "before placement" and self.with_robot):
            draw_picture(STAGE_IMG, True, 'SHIPS PLACEMENT', BLACK, subtitle, WIDTH / 2, HEIGHT /2)
        else:
            draw_picture(STAGE_IMG, True, f'PLAYER {self.now_play + 1}', BLACK, subtitle, WIDTH / 2, HEIGHT /2 - 100)
            draw_picture(STAGE_IMG, False, 'SHIP PLACEMENT', BLACK, subtitle, WIDTH / 2, HEIGHT /2)

        pygame.display.flip()
        time.sleep(SLEEP_TIME)

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

        #Переворачивание экрана
        pygame.display.flip()
        if (self.with_robot and self.now_play == 1):
            time.sleep(SLEEP_TIME / 2)
         
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
        self.block = True
        self.update()
        self.player[0].clear()
        self.player[1].clear()
        
        if(self.kill_now):
            draw_picture(HIT_IMG, True, 'SUNK!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            BATTLE_SOUND.play()
        elif (self.hit_now):
            draw_picture(HIT_IMG, True, 'HIT!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            BATTLE_SOUND.play()
        else:
            draw_picture(PAST_IMG, True, 'MISS!', CORNSILK, big, WIDTH / 2, HEIGHT /2)
            WATER_SOUND.play()

        pygame.display.flip()
        time.sleep(SLEEP_TIME * 1.35)
        
        if (not self.hit_now):
            self.now_play = (self.now_play + 1) % 2
        
        self.hit_now = False
        self.kill_now = False

    def physics(self):
        self.block = False
        self.update()

        draw_picture(BACKGROUND_IMG, True, self.info_question[0], BLACK, main, WIDTH/2, HEIGHT/8)
        draw_picture(BACKGROUND_IMG, False, self.info_question[1], BLACK, main, WIDTH/2, HEIGHT/8 + 75)

        our_buttons.draw([False, False, False, True, True, True, True, False, False], self.info_question[2], self.info_question[3])

        pygame.display.flip()

        if ((our_buttons.button['first_variant'].color == RED and our_buttons.button['first_variant'].is_click) 
            or (our_buttons.button['second_variant'].color == RED  and our_buttons.button['second_variant'].is_click)
            or (our_buttons.button['third_variant'].color == RED and our_buttons.button['third_variant'].is_click)
            or (our_buttons.button['forth_variant'].color == RED and our_buttons.button['forth_variant'].is_click)):
            self.now_play = (self.now_play + 1) % 2
            WRONG_ANSWER.play()
            time.sleep(SLEEP_TIME)
        if ((our_buttons.button['first_variant'].color == GREEN and our_buttons.button['first_variant'].is_click) 
            or (our_buttons.button['second_variant'].color == GREEN  and our_buttons.button['second_variant'].is_click)
            or (our_buttons.button['third_variant'].color == GREEN and our_buttons.button['third_variant'].is_click)
            or (our_buttons.button['forth_variant'].color == GREEN and our_buttons.button['forth_variant'].is_click)):
            RIGHT_ANSWER.play()
            time.sleep(SLEEP_TIME)

    def end(self):
        self.block = False
        self.update()
        
        draw_picture(CARD_IMG, True, 'Bot has won', BLACK, title, WIDTH / 2, HEIGHT /2)
        if (self.with_robot and self.now_play % 2 + 1 == 2):
            draw_picture(CARD_IMG, True, 'Bot has won', BLACK, title, WIDTH / 2, HEIGHT /2)
        elif (self.with_robot and self.now_play % 2 + 1 == 1):
            draw_picture(CARD_IMG, True, 'Player has won', BLACK, title, WIDTH / 2, HEIGHT /2)
        else:
            draw_picture(CARD_IMG, True, f'Player {self.now_play % 2 + 1} has won', BLACK, title, WIDTH / 2, HEIGHT /2)
        draw_picture(CARD_IMG, False, f'Do you want to play again?', BLACK, subtitle, WIDTH / 2, HEIGHT /2 + 200)
        our_buttons.draw([False, False, False, False, False, False, False, True, True])
        
        pygame.display.flip()

        if (our_buttons.button['yes'].is_click):
                self.play = -1
        if (our_buttons.button['no'].is_click):
                self.play = -2