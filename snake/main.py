

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from player import Player, Snake
import logic


prize = Group()

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    cfg = Settings()
    screen = pygame.display.set_mode(cfg.screen_size)
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    head = Player(cfg, screen, pygame.Rect(0, 0, 32, 32), 'darkcyan')
    head.to_center()
    snake = Snake(head)
    body = Player(cfg, screen, pygame.Rect(0, 320, 32, 32), 'green')
    prize.add(body)


    timer = pygame.time.Clock()
    while True:
        timer.tick(120)
        # Отслеживание событий клавиатуры и мыши.
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                snake.to_top()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                snake.to_right()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                snake.to_left()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                snake.to_down()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                snake.stop()
        screen.fill(pygame.Color('grey'))
        snake.draw(screen)
        prize.draw(screen)
        snake.update()
        # print(len(snake))
        logic.update_head(head, prize, snake)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()