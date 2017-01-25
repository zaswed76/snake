from direct import Direct
import pygame
from pygame.sprite import Sprite


class Snake(list):
    def __init__(self, body):
        super().__init__()
        self.append(body)

    @property
    def last_body(self):
        return self[-1]

    @property
    def head(self):
        return self[0]

    def add(self, body):
        self.__coordinates_accession(body)
        self.append(body)
        # self.stop()

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
        for s in self[1:]:
            s.update(self[0].direct)

    def __coordinates_accession(self, body):
        last_body = self.last_body
        direct = last_body.direct  # куда двигалсся в момент столкновения
        if str(direct) == Direct.Right:
            body.rect.right = last_body.rect.left
            body.rect.centery = last_body.rect.centery
            body.center_x = body.rect.centerx
            body.center_y= body.rect.centery
        elif str(direct) == Direct.Left:
            body.rect.left = last_body.rect.right
            body.rect.centery = last_body.rect.centery
        elif str(direct) == Direct.Top:
            body.rect.centerx = last_body.rect.centerx
            body.rect.top = last_body.rect.bottom
        elif str(direct) == Direct.Down:
            body.rect.centerx = last_body.rect.centerx
            body.rect.bottom = last_body.rect.top


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
        direct = args[0]
        if str(direct) == Direct.Right:
            self.center_x += self.speedx
        elif str(direct) == Direct.Top:
            self.center_y -= self.speedy
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

class Head(Body):
    def __init__(self, cfg, screen, rect, color, *groups):
        super().__init__(cfg, screen, rect, color, *groups)
        self.direct = Direct()

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