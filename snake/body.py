
from direct import Direct
import pygame
from pygame.sprite import Sprite

class Snake(list):
    def __init__(self, head):
        super().__init__()
        self.append(head)



    def add(self, body):
        x = self[0].rect.centerx - 32
        y = self[0].rect.centery
        body.rect.centerx = x
        body.rect.centery = y
        self.append(body)

    def to_right(self):
        self[0].direct.right = True

    def to_left(self):
        self[0].direct.left = True

    def to_top(self):
        self[0].direct.top = True

    def to_down(self):
        self[0].direct.down = True

    def stop(self):
        self[0].direct.stop()

    def draw(self, screen):
        for sp in self:
            sp.draw(screen)

    def update(self):
        self[0].update()
        # for s in self[1:]:
        #     s.update_2()




class Body(Sprite):
    def __init__(self, cfg, screen, rect, color, width=0, *groups):
        super().__init__(*groups)
        self.cfg = cfg

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = pygame.Color(color)
        self.image = pygame.Surface(rect.size)
        self.image.fill(self.color)
        self.width = width
        self.rect = rect
        self.direct = Direct()

        # Каждый новый корабль появляется у нижнего края экрана.

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.speedx = cfg.speed
        self.speedy = cfg.speed

    def to_center(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, *args):
        self.check_wall()
        if self.direct.right:
            self.center_x += self.speedx
        elif self.direct.left:
            self.center_x -= self.speedx
        elif self.direct.top:
            self.center_y -= self.speedy
        elif self.direct.down:
            self.center_y += self.speedy

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def old_coordinate(self):
        return (self.rect.centerx, self.rect.centery)

    def check_wall(self):
        """ проверка на столкновение с краем """
        if (self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom or
            self.rect.left < 0 or self.rect.right > self.screen_rect.right):
            self.direct.stop()
            self.to_center()

