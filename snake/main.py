

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from player import Player

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode(cfg.screen_size)
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    player = Player(cfg, screen, pygame.Rect(0, 0, 32, 32), 'darkcyan')
    timer = pygame.time.Clock()
    while True:
        timer.tick(120)
        # Отслеживание событий клавиатуры и мыши.
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                player.stop()
                player.speedy = - cfg.speed
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                player.stop()
                player.speedx = cfg.speed
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                player.stop()
                player.speedx = - cfg.speed
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                player.stop()
                player.speedy = cfg.speed
        screen.fill(pygame.Color('grey'))
        player.draw(screen)
        player.update()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()