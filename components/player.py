import pygame
from utils.settings import PLAYER_SPEED
# TODO .convert_alpha()
player = pygame.image.load('assets/images/player.png')
player_rect = player.get_rect()
player_speed = PLAYER_SPEED