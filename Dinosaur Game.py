import os

import pygame

WIDTH, HEIGHT = 1200, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

WHITE = (255,255,255)

FPS = 60

RUN1 = pygame.image.load(os.path.join('Assets', 'run-1.png'))
RUN2 = pygame.image.load(os.path.join('Assets', 'run-2.png'))
DUCK1 = pygame.image.load(os.path.join('Assets', 'duck-1.png'))
DUCK1 = pygame.image.load(os.path.join('Assets', 'duck-1.png'))
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

RUN1 = pygame.transform.scale(RUN1, (RUN1.get_width()/2, RUN1.get_height()/2))
RUN2 = pygame.transform.scale(RUN2, (RUN2.get_width()/2, RUN2.get_height()/2))
GROUND = pygame.transform.scale(GROUND, (GROUND.get_width()/2, GROUND.get_height()/2))


def draw_window(dino, dino_coords, floor, cacti):
    WIN.fill(WHITE)
    WIN.blit(dino, (dino_coords.x, dino_coords.y))
    WIN.blit(GROUND, (0, 280))
    pygame.display.update()


def main():
    grav_acc = 1
    dino_vel = 0
    time = 0
    dino_coords = pygame.Rect(20, 245, RUN1.get_width(), RUN1.get_height())
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            if dino_vel == 0:
                dino_vel = -12

        if dino_vel != 0:
            dino_coords.y = 245+dino_vel*time+0.5*grav_acc*time*time
            if dino_coords.y >= 245:
                dino_vel = 0
                time=0
            time=time+0.5
            if keys_pressed[pygame.K_DOWN]:
                time=time+0.5
        draw_window(RUN1, dino_coords, GROUND, SMALL1)

    pygame.quit()


if __name__ == "__main__":
    main()