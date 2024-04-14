import pygame
import time
from src.button import *
from src.game import *

pygame.init()

def game_play():
    new_game = Game()
    pygame.mixer.music.play(-1)
    
    our_buttons.refresh([False, False, True, True, True, True, True, True, True]) #все заблокированы только кнопки "с роботом" или "без робота"

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            #проверка, что окно не хотят закрыть
            if event.type == pygame.QUIT:
                return 0

        match new_game.stage:
            case 'start':
                new_game.start()
                if (our_buttons.button['with_robot'].is_click):
                    new_game.stage = "placement of ships robot"
                    our_buttons.refresh([True]*9) #всё заблокировано
                   
                elif (our_buttons.button['no_robot'].is_click):
                    new_game.stage = "before placement"
                    our_buttons.refresh([True]*9) #всё заблокировано

            case "placement of ships robot":
                new_game.robot_placement()
                new_game.stage = "before placement"
                our_buttons.refresh([True]*9) #всё заблокировано
            
            case "before placement":
                new_game.pause()
                new_game.stage = 'placement of ships'
                our_buttons.refresh([True, True, False, True, True, True, True, True, True]) #не заблокирована кнопка "подтверждение ввода"

            case 'placement of ships':
                new_game.placement_of_ships()
                if (our_buttons.button['confirm'].is_click):
                    if(not new_game.player[new_game.now_play].field.check()):
                        new_game.player[new_game.now_play].field.clear()
                        new_game.stage = 'repeat'

                    elif (new_game.with_robot or new_game.now_play == 1):
                        new_game.stage = "before game"
                    else:
                        new_game.stage = "before placement"

                    our_buttons.refresh([True]*9) #всё заблокировано

                
            case "before game":
                new_game.pause()
                new_game.stage = "move"
                our_buttons.refresh([True]*9) #всё заблокировано

            case 'move':
                new_game.move()
                if (new_game.player[(new_game.now_play + 1) % 2].change):
                    new_game.stage = 'analisis'
                    our_buttons.refresh([True]*9) #всё заблокировано

            case 'analisis':
                flag = ((new_game.hit_now or new_game.kill_now) and not (new_game.with_robot and new_game.now_play == 1))
                new_game.analisis()
                if (flag):
                    new_game.stage = "question"
                    random_formula = formulas[random.randint(0, len(formulas) - 1)]
                    new_question = Question(random_formula[0], random_formula[1], random_formula[2])
                    new_game.info_question = new_question.creat_question()
                    our_buttons.refresh([True, True, True, False, False, False, False, True, True]) #разблокированы только варианты ответов
                else:
                    new_game.stage = "move"
                    our_buttons.refresh([True]*9) #всё заблокировано

                if (new_game.player[0].cnt_ships == 0 or new_game.player[1].cnt_ships == 0):
                    new_game.stage = 'end'
                    our_buttons.refresh([True, True, True, True, True, True, True, False, False]) #разблокированы кнопки "да" и "нет"

            case 'question':
                new_game.physics()
                if (our_buttons.button['first_variant'].is_click or our_buttons.button['second_variant'].is_click or our_buttons.button['third_variant'].is_click or our_buttons.button['forth_variant'].is_click):
                    new_game.stage = "move"
                    time.sleep(SLEEP_TIME)
                    our_buttons.refresh([True]*9) #всё заблокировано
    
            case 'repeat':
                new_game.repeat()
                new_game.stage = 'placement of ships'
                our_buttons.refresh([True, True, False, True, True, True, True, True, True]) #не заблокирована кнопка "подтверждение ввода"

            case 'end':
                new_game.end()
                if (new_game.play == -1):
                    our_buttons.refresh([True]*9) #всё заблокировано
                    return 1
                elif (new_game.play == -2):
                    our_buttons.refresh([True]*9) #всё заблокировано
                    return 0