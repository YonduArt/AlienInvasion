import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Создание пули'''
    def __init__(self, ai):
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        '''Перемещает снаряд по экрану'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''Вывод снаряда на экран'''
        pygame.draw.rect(self.screen, self.color, self.rect)