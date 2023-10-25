import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'assets/background.png'
sprite_image_filename = 'assets/token.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
sprite = pygame.transform.scale(sprite, (100, 100))

# objeto clock
clock = pygame.time.Clock()

# coordenada do sprite
x1 = 0
x2 = 0

# velocidade em pixels por segundo
speed = 250

frame_no = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x1, 100))
    screen.blit(sprite, (x2, 300))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x1 += distance_moved

    if frame_no % 5 == 0:
        distance_moved = time_passed_seconds * speed
        x2 += distance_moved * 5

    if x1 > 640:
        x1 -= 640
    if x2 > 640:
        x2 -= 640

    pygame.display.update()
    frame_no += 1
