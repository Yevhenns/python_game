import pygame
import random

def create_enemy(width, height):
    enemy = pygame.transform.scale(pygame.image.load(
        'assets/images/enemy.png').convert_alpha(), (150, 50))
    enemy_rect = pygame.Rect(
        width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]