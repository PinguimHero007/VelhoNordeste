import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, WIN_WIDTH, WIN_HEIGHT, FINAL_POS


class Final:


    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/FinalBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show_final(self):
        pygame.mixer_music.load('./asset/FinalBg.mp3')
        pygame.mixer_music.play()
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.final_text(48, 'Obrigado por Jogar', C_BLACK, FINAL_POS['Title'])
            pygame.display.flip()
            pass
    def final_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
            self.window.blit(source=text_surf, dest=text_rect)
