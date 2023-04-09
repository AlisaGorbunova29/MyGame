import pygame
import time
import os 

# размеры поля
WIDTH = 1050
HEIGHT = 800
FPS = 30

#Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Морской бой")
clock = pygame.time.Clock()


# Задаем цвета
MIDNIGTHBLUE = (25, 25, 112)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
LIGHTBLUE = (0, 206, 209 )
LIGHTYELLOW = (255, 255, 224)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
LIGHTCORAL = (240, 128, 128)
RED = (255, 0, 0)
CORNSILK = (255, 248, 220)

#путь к файлам
game_folder = os.path.dirname(__file__)

#шрифты
main = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 32)
text_button = pygame.font.Font(os.path.join(game_folder, 'text', 'main.ttf'), 40)
title = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 80)
subtitle = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 60)
big = pygame.font.Font(os.path.join(game_folder, 'text', 'title.ttf'), 120)


#этап игры
NUMBER_TURNE = 0

CARD_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'card.png')).convert()
CARD_IMG = pygame.transform.scale(CARD_IMG, (WIDTH, HEIGHT))

BACKGROUND_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'background.png')).convert()
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))

WATER_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'water.png')).convert()
WATER_IMG = pygame.transform.scale(WATER_IMG, (50, 50))

SHIP_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'ship_img.png')).convert()
SHIP_IMG = pygame.transform.scale(SHIP_IMG, (50, 50))

HIT_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'hit.png')).convert()
HIT_IMG = pygame.transform.scale(HIT_IMG, (WIDTH, HEIGHT))

PAST_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'past.png')).convert()
PAST_IMG = pygame.transform.scale(PAST_IMG, (WIDTH, HEIGHT))

STAGE_IMG = pygame.image.load(os.path.join(game_folder, 'img', 'stage.png')).convert()
STAGE_IMG = pygame.transform.scale(STAGE_IMG, (WIDTH, HEIGHT))

#музыка

BACKGROUND_SOUND = pygame.mixer.music.load(os.path.join(game_folder, 'music', 'background_sound.mp3'))
pygame.mixer.music.set_volume(0.2)
WATER_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'water_sound.wav'))
BATTLE_SOUND = pygame.mixer.Sound(os.path.join(game_folder, 'music', 'battle.wav'))


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

        
class Button():
    def __init__(self,x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.flag = 0
        self.color = WHITE
        self.change = 0
        self.stage = 1
    def draw(self):
        mouse = pygame.mouse.get_pos()
        if (self.rect.collidepoint(mouse[0], mouse[1]) and self.stage != 2 and self.color == WHITE):
            pygame.draw.rect(screen, LIGHTYELLOW, self.rect)
        else:
            if (self.color == LIGHTBLUE):
                screen.blit(WATER_IMG, (self.rect.x, self.rect.y))
            elif (self.color == BLACK):
                screen.blit(SHIP_IMG, (self.rect.x, self.rect.y))
            else:
                pygame.draw.rect(screen, self.color, self.rect)
    def update(self, block):
        if (not block):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if (self.stage == 2 and self.color == YELLOW):
                self.color = WHITE
            elif (self.rect.collidepoint(mouse[0], mouse[1]) and click[0] and self.change == 0):
                if (self.stage == 1):
                    self.flag = 1
                    self.color = YELLOW
                if (self.stage == 3):
                    if (self.flag == 0):
                        self.color = LIGHTBLUE
                        self.change = NUMBER_TURNE
                    else:
                        self.color = BLACK
                        self.change = -NUMBER_TURNE


class Field():
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(x, y, width, height)
        size = 50
        self.ships = list()
        for x in range(8):
            self.ships.append(list())
            for y in range(8):
                ship = Button(self.rect.x + size * (x + 1), self.rect.y + size * (y + 1), size, size)
                self.ships[x].append(ship)
    def draw(self):
        size = 50
        for x in range(9):
            for y in range(9):
                coord = pygame.Rect(self.rect.x + size * x, self.rect.y + size * y, size, size)
                if (y == 0 and x == 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                if (y == 0 and x != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    letter = chr(ord('A') + x - 1)
                    text1 = main.render(f'{letter}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + size * x + size / 3, self.rect.y + size * y + size / 4))
                elif (x == 0 and y != 0):
                    pygame.draw.rect(screen, LIGHTBLUE, coord)
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
                    text1 = main.render(f'{y}', False, (0, 0, 0))
                    screen.blit(text1, (self.rect.x + size * x + size / 3, self.rect.y + size * y + size / 4))
                else:
                    self.ships[x - 1][y - 1].draw()
                    pygame.draw.rect(screen, MIDNIGTHBLUE, coord, 2)
    def update(self, block):
        if (not block):
            for x in range(8):
                for y in range(8):
                    self.ships[x][y].update(block)  


class Player():
    def __init__(self, x, y, width, height):
        self.field = Field(x, y, width, height)
        self.cnt_ships = 0
        self.stage = 1
        self.hit = False
        self.change = False
    def update(self, block):
        if (not block):
            self.field.update(block)
            self.change = False
            self.hit = False
            self.cnt_ships = 0
            for x in range(8):
                for y in range(8):
                    if (self.field.ships[x][y].change == NUMBER_TURNE and self.field.ships[x][y].stage == 3):
                        self.change = True
                    if (self.field.ships[x][y].change == -NUMBER_TURNE and self.field.ships[x][y].stage == 3):
                        self.change = True
                        self.hit = True
                        self.field.ships[x][y].flag = -1
                    if (self.field.ships[x][y].flag == 1):
                        self.cnt_ships += 1
    def change_stage(self, new_stage):
        self.stage = new_stage
        for x in range(8):
            for y in range(8):
                self.field.ships[x][y].stage = self.stage
    def draw(self, number):
        self.field.draw()
        text = main.render(f'Поле игрока {number}', False, (0, 0, 0))
        text_rect = text.get_rect(center=(self.field.rect.x  + self.field.rect.width / 2, self.field.rect.y - 50))
        screen.blit(text, text_rect)


def game_play():
    global NUMBER_TURNE
    
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
            player1.update(block)
            player2.update(block)
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

            player1.update(block)
            player2.update(block)

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
            player1.update(block)
            player2.update(block)
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

            player1.update(block)
            player2.update(block)

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
            player1.update(block)
            player2.update(block)
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

            player1.update(block)
            player2.update(block)

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
            player1.update(block)
            player2.update(block)
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

            player1.update(block)
            player2.update(block)

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
play = True
while (play):
    play = game_play()
pygame.quit()
