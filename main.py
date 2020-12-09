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
        self.ship = Ship(self.screen, self.settings)
        info = pygame.display.Info() // # TODO


    def main(self):
        '''Запуск основного цикла игры'''
        flag = True
        while flag:
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        '''Обрабатывает нажатия клавиш и события мыши'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    self._check_events_keydown(event)
                if event.type == pygame.KEYUP:
                    self._check_events_keyup(event)

    def _check_events_keydown(self, event, info):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            self.screen = pygame.display.set_mode((info.current_w, info.current_h)) # TODO
        elif event.key == pygame.K_F12:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))


    def _check_events_keyup(self, event):
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


    def _update_screen(self):
        '''Обновление содержимого экрана'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.main()