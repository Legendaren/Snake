import pygame

class Cell:
    EMPTY, APPLE = range(2)
    BORDER_WIDTH = 2

    def __init__(self, rect, row, column, color, item=EMPTY):
        self.rect = rect
        self.row = row
        self.column = column
        self.color = color
        self.item = item

    def collides_with(self, other_cell):
        return self.row == other_cell.row and self.column == other_cell.column

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        inner_rect = self.rect.copy()
        inner_rect.x += self.BORDER_WIDTH
        inner_rect.y += self.BORDER_WIDTH
        inner_rect.width -= self.BORDER_WIDTH
        inner_rect.height -= self.BORDER_WIDTH
        pygame.draw.rect(surface, (0, 150, 0), inner_rect)
        if self.item == self.APPLE:
            (center_x, center_y) = self.rect.center
            pygame.draw.circle(surface, (200, 0, 0), (center_x + 1, center_y + 1), int(self.rect.width / 3))

