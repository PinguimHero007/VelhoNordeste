import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import (MENU_OPTION, EVENT_ENEMY, C_WHITE, WIN_HEIGHT, C_RED, C_BLUE,EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL)
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Player2 import Player2


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL #60 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('levelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self):
        pygame.mixer_music.load('./asset/level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player,Player2, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                       self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(30, f'P1 VIDA: {ent.health}%', C_RED, (10, 10))
                if ent.name == 'Player2':
                    self.level_text(30, f'P2 VIDA: {ent.health}%', C_BLUE, (200, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy2'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        return True

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
            self.window.blit(source=text_surf, dest=text_rect)