import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    '''Управление поведением корабля'''
    def __init__(self, ai):
        '''Начальное положение корабля'''
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.image = pygame.image.load('A:/Projects/exercise/alien_invasion/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        '''Перемещает пришельцев по уровню'''
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_bound(self):
        '''Возвращает True, если пришелей находится у края экрана'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True