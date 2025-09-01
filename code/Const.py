# C
import pygame
from pygame import CONTROLLER_BUTTON_GUIDE

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 255, 0)
C_BLUE = (0, 0, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'levelBg0': 0,
    'levelBg1': 1,
    'levelBg2': 2,
    'levelBg3': 3,
    'levelBg4': 4,
    'Enemy1':3,
    'Enemy2':1,
    'Player1Shoot':5,
    'Player2Shoot':5,
    'Enemy1Shoot':5,
    'Enemy2Shoot':3,
}

ENTITY_HEALTH ={
    'levelBg0': 999,
    'levelBg1': 999,
    'levelBg2': 999,
    'levelBg3': 999,
    'levelBg4': 999,
    'Player1':100,
    'Player1Shoot':1,
    'Player2':100,
    'Player2Shoot':1,
    'Enemy1':50,
    'Enemy2':50,
    'Enemy1Shoot':1,
    'Enemy2Shoot':1,
}

ENTITY_DAMAGE = {
    'levelBg0': 0,
    'levelBg1': 0,
    'levelBg2': 0,
    'levelBg3': 0,
    'levelBg4': 0,
    'Player1': 1,
    'Player1Shoot': 25,
    'Player2': 1,
    'Player2Shoot': 25,
    'Enemy1': 1,
    'Enemy1Shoot': 5,
    'Enemy2': 1,
    'Enemy2Shoot': 5,}

ENTITY_SHOOT_DELAY = {
    'Player1': 30,
    'Player2': 30,
    'Enemy1': 40,
    'Enemy2': 80,
}
PLAYER_JUMP_DELAY = {
    'Player1':80,
    'Player2':80,
}


# M
MENU_OPTION = ('Novo Jogo',
               'Novo Jogo 2P',
               'Sair',)

#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 100000


# W
WIN_WIDTH = 600
WIN_HEIGHT = 338

FINAL_POS = {'Title': (WIN_WIDTH/2, WIN_HEIGHT),}