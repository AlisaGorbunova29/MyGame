import pygame
import time
from img import *
from object import *
from button import *
from sound import *
from config import *
from fonts import *


pygame.init()

def game_play():
     
    NUMBER_TURNE = 0

    #создали игроков
    player1 = Player(50, 100, 450, 450)
    player2 = Player(550, 100, 450, 450)

    pygame.mixer.music.play(-1)

    STAGE = -1
    button_confirm = ButtonStart(350, 650, 350, 75, 'Подвердить ввод')
    button_start = ButtonStart(350, 650, 350, 75, 'НАЧАТЬ!')
    button_yes = ButtonStart(150, 650, 350, 75, 'ДА')
    button_no = ButtonStart(600, 650, 350, 75, 'НЕТ')
    block = False
    last_move = 0
    while True:
        print(player1.change, player2.change, player1.cnt_ships, player2.cnt_ships)
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                return 0
        if (STAGE == -1):

            button_start.update(block)

            screen.blit(CARD_IMG, (0, 0))
            text = title.render('Игра "Морской бой"', False, BLACK)
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
            screen.blit(text, text_rect)
            button_start.draw()

            pygame.display.flip()

            if (button_start.is_click):
                STAGE = 0       

        elif(STAGE == 0):
            screen.blit(STAGE_IMG, (0, 0))
            text1 = title.render('ИГРОК 1', False, (0, 0, 0))
            text_rect_1 = text1.get_rect(center=(WIDTH / 2, HEIGHT /2 - 100))
            text2 = subtitle.render('РАССТАНОВКА КОРАБЛЕЙ НА ПОЛЕ', False, (0, 0, 0))
            text_rect_2 = text2.get_rect(center=(WIDTH / 2, HEIGHT /2))
            screen.blit(text1, text_rect_1)
            screen.blit(text2, text_rect_2)

            pygame.display.flip()

            time.sleep(2)

            STAGE = 1

        elif (STAGE == 1): # Расстановка кораблей первого игрока
            player1.change_stage(1)
            player2.change_stage(2)
            
            # Обновление
            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)
            button_confirm.update(block)

            #Отрисовка
            screen.blit(BACKGROUND_IMG, (0, 0))
            player1.draw(1)
            player2.draw(2)
            button_confirm.draw()

            #Переворачивание экрана
            pygame.display.flip()

            # Проверка, что игрок не подтвердил ход
            if (button_confirm.is_click):
                STAGE = 2
        elif(STAGE == 2):
            player1.change_stage(2)
            player2.change_stage(2)

            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)

            block = True 
            button_confirm.is_click = False

            screen.blit(STAGE_IMG, (0, 0))
            text1 = title.render('ИГРОК 2', False, (0, 0, 0))
            text_rect_1 = text1.get_rect(center=(WIDTH / 2, HEIGHT /2 - 100))
            text2 = subtitle.render('РАССТАНОВКА КОРАБЛЕЙ НА ПОЛЕ', False, (0, 0, 0))
            text_rect_2 = text2.get_rect(center=(WIDTH / 2, HEIGHT /2))
            screen.blit(text1, text_rect_1)
            screen.blit(text2, text_rect_2)


            pygame.display.flip()

            time.sleep(2)

            STAGE = 3
        elif (STAGE == 3): #Расстановка кораблей второго игрока
            block = False
            player1.change_stage(2)
            player2.change_stage(1)

            # Обновление
            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)
            button_confirm.update(block)

            #Отрисовка
            screen.blit(BACKGROUND_IMG, (0, 0))
            player1.draw(1)
            player2.draw(2)
            button_confirm.draw()

            #Переворачивание экрана
            pygame.display.flip()

            # Проверка, что игрок не подтвердил ход
            if (button_confirm.is_click):
                STAGE = 4
        elif(STAGE == 4):
            player1.change_stage(2)
            player2.change_stage(2)

            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)

            block = True
            button_confirm.is_click = False

            screen.blit(STAGE_IMG, (0, 0))
            text = title.render('ИГРА НАЧАЛАСЬ!', False, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
            screen.blit(text, text_rect)

            pygame.display.flip()

            time.sleep(2)
            NUMBER_TURNE += 1
            STAGE = 5
        elif (STAGE == 5): #Ход первого игрока
            block = False
            player1.change_stage(2)
            player2.change_stage(3)

            # Обновление
            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)
            button_confirm.update(block)

            #Отрисовка
            screen.blit(BACKGROUND_IMG, (0, 0))
            player1.draw(1)
            player2.draw(2)
            button_confirm.draw()

            #Переворачивание экрана
            pygame.display.flip()


            if (player2.hit == False and player2.change == True):
                STAGE = 8
                last_move = 1
            elif (player2.hit == True and player2.change == True):
                STAGE = 6
                last_move = 1
        elif (STAGE == 6):
            player1.change_stage(2)
            player2.change_stage(2)

            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)

            block = True
            player1.hit = False
            player1.change = False
        
            if (last_move == 1):
                screen.blit(HIT_IMG, (0, 0))
                BATTLE_SOUND.play()
                text = big.render('ПОПАЛ!', False, CORNSILK)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
                screen.blit(text, text_rect)
            else:
                screen.blit(PAST_IMG, (0, 0))
                WATER_SOUND.play()
                text = big.render('МИМО!', False, CORNSILK)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
                screen.blit(text, text_rect)
            pygame.display.flip()
            
            time.sleep(2.7)
            
            if (last_move == 1):
                BATTLE_SOUND.stop()
            else:
                WATER_SOUND.stop()
            NUMBER_TURNE += 1

            if (player1.cnt_ships == 0 or player2.cnt_ships == 0):
                    STAGE = 9
            else:
                STAGE = 5
        elif (STAGE == 7): #Ход первого игрока
            block = False
            player1.change_stage(3)
            player2.change_stage(2)
            
            # Обновление
            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)
            button_confirm.update(block)

            #Отрисовка
            screen.blit(BACKGROUND_IMG, (0, 0))
            player1.draw(1)
            player2.draw(2)
            button_confirm.draw()

            #Переворачивание экрана
            pygame.display.flip()

            if (player1.hit == False and player1.change == True):
                STAGE = 6
                last_move = 2
            elif (player1.hit == True and player1.change == True):
                STAGE = 8
                last_move = 2
        elif (STAGE == 8):
            player1.change_stage(2)
            player2.change_stage(2)

            player1.update(block, NUMBER_TURNE)
            player2.update(block, NUMBER_TURNE)

            block = True
            player2.hit = False
            player2.change = False
            
            screen.fill(WHITE)
            if (last_move == 2):
                screen.blit(HIT_IMG, (0, 0))
                BATTLE_SOUND.play()
                text = big.render('ПОПАЛ!', False, CORNSILK)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
                screen.blit(text, text_rect)
            else:
                screen.blit(PAST_IMG, (0, 0))
                WATER_SOUND.play()
                text = big.render('МИМО!', False, CORNSILK)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT /2))
                screen.blit(text, text_rect)
            pygame.display.flip()
            
            time.sleep(2.7)
            
            if (last_move == 2):
                BATTLE_SOUND.stop()
            else:
                WATER_SOUND.stop()

            NUMBER_TURNE += 1
            if (player1.cnt_ships == 0 or player2.cnt_ships == 0):
                    STAGE = 9
            else:
                STAGE = 7
        if (STAGE == 9):
            block = False
            button_yes.update(block)
            button_no.update(block)

            screen.blit(CARD_IMG, (0, 0))
            text1 = title.render(f'Победил игрок {last_move}', False, (0, 0, 0))
            text_rect_1 = text1.get_rect(center=(WIDTH / 2, HEIGHT /2 - 50))
            screen.blit(text1, text_rect_1)

            text2 = subtitle.render(f'Хотите сыграть ещё раз?', False, (0, 0, 0))
            text_rect_2 = text1.get_rect(center=(WIDTH / 2 - 25, HEIGHT /2 + 200))
            screen.blit(text2, text_rect_2)

            button_yes.draw()
            button_no.draw()

            pygame.display.flip()

            if (button_yes.is_click):
                return 1
            if (button_no.is_click):
                return 0