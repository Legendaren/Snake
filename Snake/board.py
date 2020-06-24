import pygame, random
import direction as dir
from cell import Cell

class Board:
    OFFSET_TOP = 40

    def __init__(self, color, screen_size, size=(20, 15)):
        self.color = color
        self.size = size
        self.cells = []
        self.cell_width = round(screen_size[0] / size[0])
        self.cell_height = round((screen_size[1] - self.OFFSET_TOP) / size[1])
        self.score = 0
        self.init_cells()
        self.apple_cell = None
        self.randomize_apple()

    def init_cells(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                rect = pygame.Rect(self.cell_width * row, self.cell_height * col + self.OFFSET_TOP, self.cell_width, self.cell_height)
                cell = Cell(rect, row, col, self.color)
                self.cells.append(cell)

    def collision_apple(self, cell):
        return self.apple_cell is not None and cell.collides_with(self.apple_cell)

    def cell_at_pos(self, row, col):
        index = self.size[1]*row + col
        return self.cells[index]

    def next_cell(self, cell, direction):
        (row_step, col_step) = dir.direction_dict[direction]
        next_row = cell.row + row_step
        next_col = cell.column + col_step
        if next_row > self.size[0] - 1:
            next_row = 0
        elif next_row < 0:
            next_row = self.size[0] - 1
        if next_col > self.size[1] - 1:
            next_col = 0
        elif next_col < 0:
            next_col = self.size[1] - 1
        return self.cell_at_pos(next_row, next_col)

    def random_cell(self):
        random_row = random.randrange(self.size[0])
        random_col = random.randrange(self.size[1])
        return self.cell_at_pos(random_row, random_col)

    def randomize_apple(self):
        if self.apple_cell is not None:
            self.apple_cell.item = Cell.EMPTY
        random_cell = self.random_cell()
        random_cell.item = Cell.APPLE
        self.apple_cell = random_cell

    def update(self):
        pass

    def draw(self, surface):
        for cell in self.cells:
            cell.draw(surface)