import pygame
from src.button import *
from src.game import *

pygame.init()

def game_play():
    new_game = Game()
    pygame.mixer.music.play(-1)
    
    refresh()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            #проверка, что окно не хотят закрыть
            if event.type == pygame.QUIT:
                return 0

        match new_game.stage:
            case 'start':
                new_game.start()
                if (button_with_robot.is_click):
                    new_game.stage = "placement of ships robot"
                elif (button_no_robot.is_click):
                    new_game.stage = "before placement"

            case "placement of ships robot":
                new_game.robot_placement()
                new_game.stage = "before placement"
            
            case "before placement":
                new_game.pause()
                new_game.stage = 'placement of ships'

            case 'placement of ships':
                new_game.placement_of_ships()
                if (button_confirm.is_click):
                    if(not new_game.player[new_game.now_play].field.check()):
                        new_game.player[new_game.now_play].field.clear()
                        new_game.stage = 'repeat'
                    elif (new_game.with_robot or new_game.now_play == 1):
                        new_game.stage = "before game"
                    else:
                        new_game.stage = "before placement"
                
            case "before game":
                new_game.pause()
                new_game.stage = "move"
            case 'move':
                new_game.move()
                if (new_game.player[(new_game.now_play + 1) % 2].change):
                    new_game.stage = 'analisis'
            case 'analisis':
                new_game.analisis()
                new_game.stage = "move"
                if (new_game.player[0].cnt_ships == 0 or new_game.player[1].cnt_ships == 0):
                    new_game.stage = 'end'
            case 'repeat':
                new_game.repeat()
                new_game.stage = 'placement of ships'
            case 'end':
                new_game.end()
                if (new_game.play == -1):
                    return 1
                elif (new_game.play == -2):
                    return 0