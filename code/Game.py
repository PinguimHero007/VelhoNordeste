import sys

import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Final import Final
from code.Level import Level
from code.Menu import Menu
import numpy as np

class Game:


    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return:
                    final = Final(self.window)
                    final.show_final()

            if menu_return == MENU_OPTION[1]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return:
                    final = Final(self.window)
                    final.show_final()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
