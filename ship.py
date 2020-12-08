import pygame

class Ship():
    '''Управление поведением корабля'''
    def __init__(self, ai_game):
        '''Начальное положение корабля'''
        self.screen = ai_game.screen()
        self.screen_rect = ai_game.screen.rect()

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blittime(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)


