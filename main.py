import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from utils.colors import RED
from utils.settings import  SCREEN_WIDTH, SCREEN_HEIGHT
from components.player import player, player_rect, player_speed 

pygame.init()

FPS = pygame.time.Clock()
screen = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)

def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load(
        'assets/images/enemy.png').convert_alpha(), (150, 50))
    enemy_rect = pygame.Rect(
        width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


def create_bonus():
    bonus = pygame.transform.scale(
        pygame.image.load('assets/images/bonus.png').convert_alpha(), (100, 150))
    bonus_rect = pygame.Rect(random.randint(
        0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(4, 6)
    return [bonus, bonus_rect, bonus_speed]


bg = pygame.transform.scale(pygame.image.load(
    'assets/images/background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

scores = 0
enemies = []
bonuses = []

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append((create_enemy()))
        if event.type == CREATE_BONUS:
            bonuses.append((create_bonus()))

    pressed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True, RED), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= height:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)

    if pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)

    if pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move(-player_speed, 0)

    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)

    pygame.display.flip()
