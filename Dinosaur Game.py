import copy
import os
import random
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 200
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

WHITE = (255, 255, 255)
HIGH = (117, 117, 117)
CURR = (83, 83, 83)

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
DEAD = pygame.transform.scale(DEAD, (DEAD.get_width() / 2, DEAD.get_height() / 2))

GROUND = pygame.transform.scale(GROUND, (GROUND.get_width() / 2, GROUND.get_height() / 2))
CLOUD = pygame.transform.scale(CLOUD, (CLOUD.get_width() / 2, CLOUD.get_height() / 2))
RESTART = pygame.transform.scale(RESTART, (RESTART.get_width() / 2, RESTART.get_height() / 2))

BIRD1 = pygame.transform.scale(BIRD1, (BIRD1.get_width() / 2, BIRD1.get_height() / 2))
BIRD2 = pygame.transform.scale(BIRD2, (BIRD2.get_width() / 2, BIRD2.get_height() / 2))

SMALL1 = pygame.transform.scale(SMALL1, (SMALL1.get_width() / 2, SMALL1.get_height() / 2))
SMALL2 = pygame.transform.scale(SMALL2, (SMALL2.get_width() / 2, SMALL2.get_height() / 2))
SMALL3 = pygame.transform.scale(SMALL3, (SMALL3.get_width() / 2, SMALL3.get_height() / 2))

LARGE1 = pygame.transform.scale(LARGE1, (LARGE1.get_width() / 2, LARGE1.get_height() / 2))
LARGE2 = pygame.transform.scale(LARGE2, (LARGE2.get_width() / 2, LARGE2.get_height() / 2))
LARGE3 = pygame.transform.scale(LARGE3, (LARGE3.get_width() / 2, LARGE3.get_height() / 2))

JUMP_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'jump.wav'))
POINT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'point.wav'))
DIE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'die.wav'))

FONT = pygame.font.Font(os.path.join('Assets', 'PressStart2P-Regular.ttf'), 12)


def draw_window(dino, dino_coords, floor, floor_coords, obst, clouds):
    for key, value in obst.items():
        WIN.blit(key, (value.x, value.y))
    for key, value in clouds.items():
        WIN.blit(key, (value.x, value.y))
    WIN.blit(dino, (dino_coords.x, dino_coords.y))
    WIN.blit(floor, (floor_coords.x, floor_coords.y))
    WIN.blit(floor, (floor_coords.x + 1200, floor_coords.y))
    pygame.display.update()


def main():
    dead = False
    high_score = 0
    curr_score = 0
    grav_acc = 1.6
    dino_vel = 0
    time = 0
    obst = {}
    clouds = {}
    dino_count = 0
    point_count = 0
    obst_count = 0
    cloud_count = 0
    dino_coords = pygame.Rect(20, 145, RUN1.get_width(), RUN1.get_height())
    dino_duck_coords = pygame.Rect(20, 160, DUCK1.get_width(), DUCK1.get_height())
    floor_coords = pygame.Rect(0, 180, GROUND.get_width(), GROUND.get_height())
    bird_coords = pygame.Rect(650, 145, BIRD1.get_width(), BIRD1.get_height())
    bird_low_coords = pygame.Rect(650, 125, BIRD1.get_width(), BIRD1.get_height())
    cacti_small1_coords = pygame.Rect(650, 155, SMALL1.get_width(), SMALL1.get_height())
    cacti_small2_coords = pygame.Rect(650, 155, SMALL2.get_width(), SMALL2.get_height())
    cacti_small3_coords = pygame.Rect(650, 155, SMALL3.get_width(), SMALL3.get_height())
    cacti_large1_coords = pygame.Rect(650, 145, LARGE1.get_width(), LARGE1.get_height())
    cacti_large2_coords = pygame.Rect(650, 145, LARGE2.get_width(), LARGE2.get_height())
    cacti_large3_coords = pygame.Rect(650, 145, LARGE3.get_width(), LARGE3.get_height())
    restart_coords = pygame.Rect(300 - RESTART.get_width() / 2, 100 - RESTART.get_width() / 2, RESTART.get_width(),
                                 RESTART.get_height())
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if restart_coords.x < x and restart_coords.x + restart_coords.w > x and restart_coords.y < y and restart_coords.h + restart_coords.y > y:
                    obst.clear()
                    high_score = curr_score
                    curr_score = 0
                    dead = False
                    dino_coords.y = 145

        if not dead:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE]:
                if dino_vel == 0:
                    pygame.mixer.Sound.play(JUMP_SOUND)
                    pygame.mixer.music.stop()
                    dino_vel = -15

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
            if keys_pressed[pygame.K_DOWN] and dino_coords.y == 145:
                dino_sprite = DUCK2
                dino_info = dino_duck_coords

            dino_count = dino_count + 1
            if dino_count <= FPS / 10:
                dino_sprite = RUN2
                if keys_pressed[pygame.K_DOWN] and dino_coords.y == 145:
                    dino_sprite = DUCK2
            dino_count = dino_count % (FPS / 5)

            cloud_count = cloud_count + 1
            if cloud_count >= random.randint(100, 150):
                cloud_box = pygame.Rect(650, random.randint(30, 50), CLOUD.get_width(), CLOUD.get_height())
                clouds[copy.copy(CLOUD)] = cloud_box
                cloud_count = 0

            obst_count = obst_count + 1
            if obst_count >= random.randint(50, 100):
                type = random.randint(0, 10)
                if type <= 3:
                    height = random.randint(0, 1)
                    if height == 0:
                        obst[copy.copy(BIRD1)] = copy.copy(bird_low_coords)
                    else:
                        obst[copy.copy(BIRD2)] = copy.copy(bird_coords)
                else:
                    size = random.randint(0, 1)
                    cact = random.randint(1, 3)
                    if size == 0:
                        if cact == 1:
                            obst[copy.copy(SMALL1)] = copy.copy(cacti_small1_coords)
                        elif cact == 2:
                            obst[copy.copy(SMALL2)] = copy.copy(cacti_small2_coords)
                        else:
                            obst[copy.copy(SMALL3)] = copy.copy(cacti_small3_coords)
                    else:
                        if cact == 1:
                            obst[copy.copy(LARGE1)] = copy.copy(cacti_large1_coords)
                        elif cact == 2:
                            obst[copy.copy(LARGE2)] = copy.copy(cacti_large2_coords)
                        else:
                            obst[copy.copy(LARGE3)] = copy.copy(cacti_large3_coords)
                obst_count = 0

            point_count = point_count + 1
            if point_count == 6:
                curr_score = curr_score + 1
                point_count = 0

            if curr_score != 0 and curr_score % 100 == 0:
                pygame.mixer.Sound.play(POINT_SOUND)
                pygame.mixer.music.stop()

            pygame.display.set_icon(dino_sprite)

            for key, value in clouds.items():
                value.x = value.x - 2

            for i in list(clouds.keys()):
                if clouds[i].x <= -100:
                    del clouds[i]

            for key, value in obst.items():
                value.x = value.x - 5

            for i in list(obst.keys()):
                if obst[i].x <= -100:
                    del obst[i]

            floor_coords.x = floor_coords.x - 5
            if floor_coords.x <= -1200:
                floor_coords.x = 0

            WIN.fill(WHITE)

            for key, value in obst.items():
                if dino_info.x + 10 < value.x + value.w and dino_info.x + 10 + dino_info.w - 20 > value.x and dino_info.y + 10 < value.y + value.h and dino_info.h - 20 + dino_info.y + 10 > value.y:
                    pygame.mixer.Sound.play(DIE_SOUND)
                    pygame.mixer.music.stop()
                    game_over_text = FONT.render('G A M E  O V E R', True, CURR)
                    game_over_rect = game_over_text.get_rect()
                    game_over_rect.center = (300, 70)
                    WIN.blit(game_over_text, game_over_rect)
                    WIN.blit(RESTART, (restart_coords.x, restart_coords.y))
                    dino_sprite = DEAD
                    dead = True

            if curr_score > 100000:
                pygame.mixer.Sound.play(DIE_SOUND)
                pygame.mixer.music.stop()
                game_over_text = FONT.render('Y O U \' R E  T O O  G O O D', True, CURR)
                game_over_rect = game_over_text.get_rect()
                game_over_rect.center = (300, 70)
                WIN.blit(game_over_text, game_over_rect)
                WIN.blit(RESTART, (restart_coords.x, restart_coords.y))
                dino_sprite = DEAD
                dead = True

            high_score_text = FONT.render(f'HI {str(high_score).zfill(6)}', True, HIGH)
            curr_score_text = FONT.render(f'{str(curr_score).zfill(6)}', True, CURR)
            high_rect = high_score_text.get_rect()
            curr_rect = curr_score_text.get_rect()
            curr_rect.topright = (590, 10)
            high_rect.topright = (500, 10)

            WIN.blit(curr_score_text, curr_rect)
            WIN.blit(high_score_text, high_rect)

            draw_window(dino_sprite, dino_info, GROUND, floor_coords, obst, clouds)

    pygame.quit()


if __name__ == "__main__":
    main()
