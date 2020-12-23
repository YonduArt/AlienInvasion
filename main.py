import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion():
    '''Основной класс игры'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.title_name)
        self.stats = GameStats(self)
        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def main(self):
        '''Запуск основного цикла игры'''
        self.flag = True # TODO
        while self.flag:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()

    def _check_events(self):
        '''Обрабатывает нажатия клавиш и события мыши'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_events_keydown(event)
                if event.type == pygame.KEYUP:
                    self._check_events_keyup(event)

    def _check_events_keydown(self, event):
        '''Подфункция проверяет нажатие клавиши'''
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            self.screen = pygame.display.set_mode((1920, 1080)) # TODO
        elif event.key == pygame.K_F12:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        elif event.key == pygame.K_f:
            self._fire_bullet()

    def _check_events_keyup(self, event):
        '''Подфункция проверяет отпускание клавиши'''
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self):
        '''Создание нового снаряда и включение его в группу bullet'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Удаляет снаряд, если вышел за края экрана'''
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''Обработка коллизий снарядов с пришельцами'''
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()

    def _create_alien(self, alien_number, row_number):
        '''Создание пришельцев на экране'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        '''Создание флота пришельцев'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        '''Определяет количество рядов, помещающихся на экране'''
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Создание флота
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _update_aliens(self):
        '''Обновляет позиции всех пришельцев во флоте'''
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        '''Обрабатывает столкновение пришельца с кораблем.'''
        if self.stats.ships_left > 0:
            # Уменьшение ships_left
            self.stats.ships_left -= 1
            # Очистка спсков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # Создание нового флота и размещения корабля
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.flag = False # TODO

    def _check_fleet_edges(self):
        '''Реагирует на достижение пришельцем края экрана.'''
        for alien in self.aliens.sprites():
            if alien.check_bound():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Опускает весь флот и меняет его направление движения'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        '''Проверяет добрались ли пришельцы до нижнего края экрана'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        '''Обновление содержимого экрана'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.main()