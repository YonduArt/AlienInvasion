class Settings():
    '''Настройки игры'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.title_name = 'Alien Invasion'
        self.ship_speed = 0.75
        self.ship_limit = 3
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 3
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 - движение вправо; -1 - движение влево
        self.fleet_direction = 1