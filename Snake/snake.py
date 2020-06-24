import pygame
from collections import deque
from snake_part import SnakePart
import direction

class Snake:

    def __init__(self, cell, color, direction=direction.RIGHT):
        self.color = color
        self.direction = direction
        self.head = SnakePart(cell, (100, 230, 200))
        self.body = deque() # Deque of SnakeParts
        self.add_tail(self.tail().cell, 2)

    def move_head(self, board):
        self.head.cell = board.next_cell(self.head.cell, self.direction)

    def turn_left(self):
        self.__turn_helper(-1)

    def turn_right(self):
        self.__turn_helper(1)

    def __turn_helper(self, index_increment):
        direction_index = direction.direction_list[self.direction]
        self.direction = direction.direction_list[(direction_index+index_increment) % direction.amount]

    def tail(self):
        if self.body:
            return self.body[-1]
        return self.head

    def add_tail(self, cell, amount=1):
        for _ in range(amount):
            tail = SnakePart(cell, self.color)
            self.body.append(tail)

    def pop_tail(self):
        self.body.popleft()

    def eat(self):
        self.add_tail(self.tail().cell)

    def head_collides_with_body(self):
        collison_gen = (part.cell.collides_with(self.head.cell) for part in self.body)
        return any(collison_gen)

    def update(self, board):
        self.add_tail(self.head.cell)
        self.pop_tail()
        self.move_head(board)

    def draw(self, surface):
        self.head.draw(surface)
        for part in self.body:
            part.draw(surface)