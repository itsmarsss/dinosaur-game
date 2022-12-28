import os
from random import random

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

WHITE = (255, 255, 255)

FPS = 60

RUN1 = pygame.image.load(os.path.join('Assets', 'run-1.png'))
RUN2 = pygame.image.load(os.path.join('Assets', 'run-2.png'))
DUCK1 = pygame.image.load(os.path.join('Assets', 'duck-1.png'))
DUCK2 = pygame.image.load(os.path.join('Assets', 'duck-2.png'))
DEAD = pygame.image.load(os.path.join('Assets', 'dead.png'))
BIRD1 = pygame.image.load(os.path.join('Assets', 'bird-1.png'))
BIRD2 = pygame.image.load(os.path.join('Assets', 'bird-2.png'))
SMALL1 = pygame.image.load(os.path.join('Assets', 'small-1.png'))
SMALL2 = pygame.image.load(os.path.join('Assets', 'small-2.png'))
SMALL3 = pygame.image.load(os.path.join('Assets', 'small-3.png'))
LARGE1 = pygame.image.load(os.path.join('Assets', 'large-1.png'))
LARGE2 = pygame.image.load(os.path.join('Assets', 'large-2.png'))
LARGE3 = pygame.image.load(os.path.join('Assets', 'large-3.png'))
CLOUD = pygame.image.load(os.path.join('Assets', 'cloud.png'))
RESTART = pygame.image.load(os.path.join('Assets', 'restart.png'))
GROUND = pygame.image.load(os.path.join('Assets', 'ground.png'))

RUN1 = pygame.transform.scale(RUN1, (RUN1.get_width() / 2, RUN1.get_height() / 2))
RUN2 = pygame.transform.scale(RUN2, (RUN2.get_width() / 2, RUN2.get_height() / 2))
DUCK1 = pygame.transform.scale(DUCK1, (DUCK1.get_width() / 2, DUCK1.get_height() / 2))
DUCK2 = pygame.transform.scale(DUCK2, (DUCK2.get_width() / 2, DUCK2.get_height() / 2))
GROUND = pygame.transform.scale(GROUND, (GROUND.get_width() / 2, GROUND.get_height() / 2))

JUMP_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'jump.wav'))
POINT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'point.wav'))
DIE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'die.wav'))


def draw_window(dino, dino_coords, floor, floor_coords, cacti):
    WIN.fill(WHITE)
    WIN.blit(dino, (dino_coords.x, dino_coords.y))
    WIN.blit(GROUND, (floor_coords.x, floor_coords.y))
    WIN.blit(GROUND, (floor_coords.x + 1200, floor_coords.y))
    pygame.display.update()


def generate_cacti():
    size = random.randint(0,1)
    cact = random.randint(1,3)


def main():
    high_score = 0
    curr_score = 0
    grav_acc = 1.2
    dino_vel = 0
    time = 0
    cacti = []
    dino_count = 0
    point_count = 0
    cacti_count = 0
    dino_coords = pygame.Rect(20, 145, RUN1.get_width(), RUN1.get_height())
    dino_duck_coords = pygame.Rect(20, 160, DUCK1.get_width(), DUCK1.get_height())
    floor_coords = pygame.Rect(0, 180, GROUND.get_width(), GROUND.get_height())
    cacti_small_coords = pygame.Rect(650, 170, GROUND.get_width(), GROUND.get_height())
    cacti_small_coords = pygame.Rect(650, 170, GROUND.get_width(), GROUND.get_height())
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE]:
            if dino_vel == 0:
                pygame.mixer.Sound.play(JUMP_SOUND)
                pygame.mixer.music.stop()
                dino_vel = -12

        if dino_vel != 0:
            dino_coords.y = 145 + dino_vel * time + 0.5 * grav_acc * time * time
            if dino_coords.y >= 145:
                dino_coords.y = 145
                dino_vel = 0
                time = 0
            time = time + 0.5
            if keys_pressed[pygame.K_DOWN]:
                time = time + 0.5

        dino_sprite = RUN1
        dino_info = dino_coords
        if keys_pressed[pygame.K_DOWN]:
            dino_sprite = DUCK2
            dino_info = dino_duck_coords

        dino_count = dino_count + 1
        if dino_count <= FPS / 10:
            dino_sprite = RUN2
            if keys_pressed[pygame.K_DOWN]:
                dino_sprite = DUCK2
        dino_count = dino_count % (FPS / 5)

        cacti_count = cacti_count + 1
        if cacti_count == 120:
            cacti.append[generate_cacti()]
            cacti_count = 0

        point_count = point_count + 1
        if point_count == 6:
            curr_score = curr_score + 1;
            point_count = 0

        if curr_score != 0 and curr_score % 100 == 0:
            pygame.mixer.Sound.play(POINT_SOUND)
            pygame.mixer.music.stop()

        pygame.display.set_icon(dino_sprite)

        floor_coords.x = floor_coords.x - 5
        if floor_coords.x == -1200:
            floor_coords.x = 0

        draw_window(dino_sprite, dino_info, GROUND, floor_coords, SMALL1)

    pygame.quit()


if __name__ == "__main__":
    main()
