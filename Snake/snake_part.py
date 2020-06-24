import pygame
import direction

class SnakePart:
    def __init__(self, cell, color):
        self.cell = cell
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.cell.rect)