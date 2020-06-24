import pygame, sys, time
from game import Game
import direction

pygame.init()

#size = width, height = 640, 480
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
black = 0, 0, 0
game = Game(size, screen)
FPS = 15
delta_time = 1000 / FPS # delta time in milliseconds
pause_timer_event = pygame.USEREVENT + 1
clock = pygame.time.Clock()
elapsed_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.USEREVENT:
            game.countdown_callback()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.turn_snake_left()
            if event.key == pygame.K_RIGHT:
                game.turn_snake_right()
            """if event.key == pygame.K_UP:
                game.set_snake_direction(direction.UP)
            if event.key == pygame.K_DOWN:
                game.set_snake_direction(direction.DOWN)"""


    screen.fill(black)

    # GAME LOOP ###

    if elapsed_time > delta_time:
        game.update()
        elapsed_time = 0
    elapsed_time += clock.get_time()

    game.draw(screen)

    ###

    clock.tick()
    pygame.display.flip()
    #time.sleep(1 / FPS) # 10 FPS
