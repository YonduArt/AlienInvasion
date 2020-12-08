import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion():
    '''Основной класс игры'''
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.title_name)

        self.ship = Ship(self.screen)


    def main(self):
        '''Запуск основного цикла игры'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.main()