import pygame

from code.Const import ENTITY_SHOOT_DELAY, PLAYER_JUMP_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player2(Entity):

    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
        self.jump_delay = PLAYER_JUMP_DELAY[self.name]

    def update(self):
        pass

    #Definição de comando player e modificação de velocidade individual
    def move(self):
        self.jump_delay -= 1
        if self.jump_delay == 0:
            self.jump_delay = PLAYER_JUMP_DELAY[self.name]
            pressed = pygame.key.get_pressed()

    #Pelo amor de Deus como isso funcionou eu não sei é um milagre que eu tenha conseguido colocar "Gravidade"
            if pressed[pygame.K_w]:
                self.rect.y -= 100
            if self.rect.y <= 170:
                self.rect.y += 50
            if pressed[pygame.K_a] and self.rect.left > 0:
                self.rect.centerx -= 2
            if pressed[pygame.K_d] and self.rect.right > 0:
                self.rect.centerx += 4

        pass

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LCTRL]:
                return PlayerShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery))

        pass