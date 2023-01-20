import pygame
from pygame.constants import QUIT, K_DOWN
import random

pygame.init()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    pressed_keys = pygame.key.get_pressed()

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)

    if pressed_keys[K_DOWN]

    pygame.display.flip()
