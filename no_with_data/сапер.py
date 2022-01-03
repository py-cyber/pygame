import random

import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 80
        self.top = 100
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        colors = [pygame.Color('black'), pygame.Color('white')]
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, colors[self.board[y][x]],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size))
                pygame.draw.rect(screen, colors[1],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, width, height, n):
        super().__init__(width, height)
        self.board = [[-1] * width for _ in range(height)]
        i = 0
        while i < n:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == -1:
                self.board[y][x] = 10
                i += 1

    def open_cell(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        num = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if x + j < 0 or x + j >= self.width or y + i < 0 or y + i >= self.height:
                    continue
                if self.board[y + i][x + j] == 10:
                    num += 1
        self.board[y][x] = num
        if num == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    new_cell = x + dx, y + dy
                    if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                        continue
                    if self.board[y + dy][x + dx] == -1:
                        self.open_cell(new_cell)

    def on_click(self, cell):
        self.open_cell(cell)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, 'red', (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                                     self.cell_size, self.cell_size))
                elif self.board[y][x] >= 0:
                    font = pygame.font.Font(None, self.cell_size - 6)
                    text = font.render(f'{self.board[y][x]}', 1, 'green')
                    screen.blit(text, (x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3))

                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)


pygame.init()
size = width, height = 320, 470
screen = pygame.display.set_mode(size)
screen.fill('black')
pygame.display.set_caption('Дедушка сапёра')
board = Minesweeper(10, 15, 10)
board.set_view(10, 10, 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill('black')
    board.render(screen)
    pygame.display.flip()
