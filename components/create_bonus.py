import pygame
import random

def create_bonus(width):
    bonus = pygame.transform.scale(
        pygame.image.load('assets/images/bonus.png').convert_alpha(), (100, 150))
    bonus_rect = pygame.Rect(random.randint(
        0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(4, 6)
    return [bonus, bonus_rect, bonus_speed]