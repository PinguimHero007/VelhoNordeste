from unittest import case

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player
from code.Player2 import Player2


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'levelBg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'levelBg{i}',(0,0)))
                    list_bg.append(Background(f'levelBg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                #Posição PLayer no cenário
                return Player('Player1', (10,176))
            case 'Player2':
                # Posição PLayer no cenário
                return Player2('Player2', (100, 176))
            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH, 176))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH, 180))
        return None
