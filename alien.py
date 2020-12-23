import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Управление поведением корабля'''
    def __init__(self, ai):
        '''Начальное положение корабля'''
        super().__init__()
        self.screen = ai.screen

        self.image = pygame.image.load('A:/Projects/exercise/alien_invasion/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)