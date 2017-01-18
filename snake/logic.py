import pygame



def update_head(head, prize, snake):
    collision = pygame.sprite.spritecollideany(head, prize)
    if collision is not None:
        # snake.add(collision)
        print('Владик')
        prize.remove(collision)
