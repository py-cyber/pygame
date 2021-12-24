import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 80
        self.top = 100
        self.cell_size = 30
        self.who_go =True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        #colors = ['black', 'red', 'blue']
        for y in range(self.height):
            for x in range(self.width):
                #pygame.draw.rect(screen, colors[self.board[y][x]],
                #                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                #                  self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size - 3 + self.cell_size), 2)
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + self.cell_size - 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size + 3), 2)
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color("red"),
                        ((self.left + x * self.cell_size + 3, self.top + y * self.cell_size + 3),
                        (self.cell_size - 6, self.cell_size - 6)), 2)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell_coords):
        if self.board[cell_coords[1]][cell_coords[0]] == 0:
            if self.who_go:
                self.board[cell_coords[1]][cell_coords[0]] = 1
            else:
                self.board[cell_coords[1]][cell_coords[0]] = 2
            self.who_go = not self.who_go


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


size = width, height = 350, 450
screen = pygame.display.set_mode(size)
screen.fill('black')
board = Board(5, 7)
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
