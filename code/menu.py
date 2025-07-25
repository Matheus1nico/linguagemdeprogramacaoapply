from code.const import WIN_WIDTH, ORANGE_COLOR, MENU_OPTIONS, WHITE_COLOR
from pygame import Surface
from pygame.font import Font
from pygame import Rect
import pygame.image

class Menu:

    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        # creating menu music
        pygame.mixer.music.load('./assets/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.text_menu(60, "Mountain", ORANGE_COLOR, ((WIN_WIDTH / 2), 50))
            self.text_menu(60, "Shooter", ORANGE_COLOR, ((WIN_WIDTH / 2), 90))

            for i in range(len(MENU_OPTIONS)):
                self.text_menu(30, MENU_OPTIONS[i], WHITE_COLOR, (WIN_WIDTH / 2, 140 + 30 * i))

            pygame.display.flip()


            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Closing Window')
                    pygame.quit()  # close window
                    quit()  # end pygame

    def text_menu(self, text_size:int, text:str, text_color:tuple, text_center_position:tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size = text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center = text_center_position)
        self.window.blit(source = text_surface, dest = text_rect)