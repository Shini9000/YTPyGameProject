import time

import pygame
from sys import exit

# Starting vars
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("pyGameProject")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surface = test_font.render("Score: ", False, (0, 0, 0))
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(800, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))




# True loop
while True:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYUP:
            print('UP')
        if event.type == pygame.KEYDOWN:
            print("DOWN")
            if event.key == pygame.K_SPACE:
                print('JUMP')

    # BG surfaces
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#935af2', score_rect.inflate(0, 10))
    pygame.draw.rect(screen, '#935af2', score_rect.inflate(10, 0))
    screen.blit(score_surface, score_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')


    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('Collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())


    # Main surfaces

    # Game loop
    pygame.display.update()
    clock.tick(60)
