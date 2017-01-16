

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from player import Player, Snake

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode(cfg.screen_size)
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    head = Player(cfg, screen, pygame.Rect(0, 0, 32, 32), 'darkcyan')
    snake = Snake(head)

    timer = pygame.time.Clock()
    while True:
        timer.tick(120)
        # Отслеживание событий клавиатуры и мыши.
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                snake.stop()
                snake.speedy = - cfg.speed
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                snake.stop()
                snake.speedx = cfg.speed
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                snake.stop()
                snake.speedx = - cfg.speed
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                snake.stop()
                snake.speedy = cfg.speed
        screen.fill(pygame.Color('grey'))
        snake.draw(screen)
        snake.update()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()