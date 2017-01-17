import pygame




def update_head(head, prize):
    collision = pygame.sprite.spritecollideany(head, prize)
    if collision is not None:
        print(collision)