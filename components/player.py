import os
import pygame
from utils.settings import PLAYER_SPEED

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
IMAGE_PATH = os.path.join(PROJECT_DIR, 'assets', 'images', 'player.png')

player = pygame.image.load(IMAGE_PATH)
player_rect = player.get_rect()
player_speed = PLAYER_SPEED