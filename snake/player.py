import pygame
from pygame.sprite import Sprite


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
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.stop()

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def draw(self, screen):
        return screen.blit(self.surface, self.rect)

    def update(self, *args):
        # if self.moving_right:
            self.center_x += self.speedx
        # elif self.moving_left:
            self.center_x += self.speedx
        # elif self.moving_up:
            self.center_y += self.speedy
        # elif self.moving_down:
            self.center_y += self.speedy

            self.rect.centerx = self.center_x
            self.rect.centery = self.center_y