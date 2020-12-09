import pygame

class Ship():
    '''Управление поведением корабля'''
    def __init__(self, screen, settings):
        '''Начальное положение корабля'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.image = pygame.image.load('A:/Projects/exercise/alien_invasion/images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) # Преобразует в вещественное число
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Меняет положение если клавиша нажата'''
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left >= 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x # Присваиваем, потому что rect не берёт вещественные числа

    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)


