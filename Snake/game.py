import pygame
from snake import Snake
from board import Board
from audio_player import AudioPlayer

class Game:
    STATE_ACTIVE, STATE_PAUSED, STATE_GAMEOVER, STATE_COUNTDOWN = range(4)

    def __init__(self, screen_size, surface):
        self.state = Game.STATE_COUNTDOWN
        self.countdown_counter = 0 # Time in seconds for countdown
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.SysFont('Helvetica', 30)
        self.screen_size = screen_size
        self.surface = surface
        self.board = Board((0, 200, 0), screen_size, (40, 22))
        self.snake = Snake(self.board.random_cell(), (0, 255, 0))
        self.countdown(surface, 3)

    def set_snake_direction(self, direction):
        self.snake.direction = direction

    def turn_snake_left(self):
        self.snake.turn_left()

    def turn_snake_right(self):
        self.snake.turn_right()

    def countdown(self, surface, seconds):
        self.countdown_counter = seconds
        pygame.time.set_timer(pygame.USEREVENT, 1000)

    def countdown_callback(self):
        if self.countdown_counter <= 1:
            # Disable timer
            pygame.time.set_timer(pygame.USEREVENT, 0)
            self.state = Game.STATE_ACTIVE
        else:
            self.countdown_counter -= 1

    def draw_countdown_text(self, surface):
        font_size = 120
        countdown_font = pygame.font.SysFont('Helvetica', font_size)
        countdown_text_surface = countdown_font.render(str(self.countdown_counter), True, (255, 255, 255))
        self.draw_centered_text(surface, countdown_text_surface)

    def game_over(self, surface):
        self.state = Game.STATE_GAMEOVER
        ap = AudioPlayer.get_instance()
        ap.play("fail-trombone.mp3")

    def draw_game_over_text(self, surface):
        font_size = 120
        gameover_font = pygame.font.SysFont('Helvetica', font_size)
        gameover_text_surface = gameover_font.render("Game Over", True, (255, 255, 255))
        self.draw_centered_text(surface, gameover_text_surface)

    def draw_centered_text(self, surface, text_surface):
        center_x = self.screen_size[0] / 2
        center_y = self.screen_size[1] / 2
        text_rect = text_surface.get_rect(center=(center_x, center_y))
        text_rect.center = (center_x, center_y)
        surface.blit(text_surface, text_rect)
        pygame.display.update(text_rect)

    def reset(self):
        self.score = 0
        self.snake = Snake(self.board.random_cell(), (0, 255, 0))

    def update(self):
        if self.state == Game.STATE_GAMEOVER:
            return
        elif self.state == Game.STATE_PAUSED:
            return
        elif self.state == Game.STATE_COUNTDOWN:
            return
        self.board.update()
        self.snake.update(self.board)
        if self.board.collision_apple(self.snake.head.cell):
            self.snake.eat()
            self.board.randomize_apple()
            self.score += 1
            ap = AudioPlayer.get_instance()
            ap.play('apple_bite.ogg')
        if self.snake.head_collides_with_body():
            self.game_over(self.surface)

    def draw(self, surface):
        self.board.draw(surface)
        self.snake.draw(surface)
        self.draw_score_text(surface)
        if self.state == Game.STATE_GAMEOVER:
            self.draw_game_over_text(surface)
        elif self.state == Game.STATE_PAUSED:
            return
        elif self.state == Game.STATE_COUNTDOWN:
            self.draw_countdown_text(surface)

    def draw_score_text(self, surface):
        textsurface = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        surface.blit(textsurface, (10, 10))