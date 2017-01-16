import pygame
from pygame.sprite import Sprite

class Snake(list):
    def __init__(self, head):
        super().__init__()
        self.append(head)

    @property
    def speedy(self):
        return self[0].speedy

    @speedy.setter
    def speedy(self, v):
        for sp in self:
            sp.speedy = v

    @property
    def speedx(self):
        return self[0].speedx

    @speedx.setter
    def speedx(self, v):
        for sp in self:
            sp.speedx = v

    def stop(self):
        for sp in self:
            sp.stop()

    def draw(self, screen):
        for sp in self:
            sp.draw(screen)

    def update(self):
        for sp in self:
            sp.update()

class Player(Sprite):
    def __init__(self, cfg, screen, rect, color, width=0, *groups):
        super().__init__(*groups)
        self.cfg = cfg

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = pygame.Color(color)
        self.surface = pygame.Surface(rect.size)
        self.surface.fill(self.color)
        self.width = width
        self.rect = rect

        # Каждый новый корабль появляется у нижнего края экрана.

        self.to_start()
        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.stop()

    def to_start(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def update(self, *args):
        self.check_wall()
        self.center_x += self.speedx
        self.center_x += self.speedx
        self.center_y += self.speedy
        self.center_y += self.speedy

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def check_wall(self):
        """ проверка на столкновение """
        if (self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom or
            self.rect.left < 0 or self.rect.right > self.screen_rect.right):
            self.stop()
            self.to_start()

