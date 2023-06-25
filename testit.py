import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1 for j in range(height)] for i in range(width)]
        self.col = [[(0, 0, 0) for j in range(height)] for i in range(width)]
        self.left = 0
        self.top = 0
        self.cell_size = 25

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, 'white', (self.left + x * self.cell_size,
                                                   self.top + y * self.cell_size,
                                                   self.cell_size,
                                                   self.cell_size), self.board[x][y])
                pygame.draw.rect(screen, self.col[x][y], (self.left + x * self.cell_size + 1,
                                                   self.top + y * self.cell_size + 1,
                                                   self.cell_size - 2,
                                                   self.cell_size - 2))

    def get_coords(self, position):
        x, y = position
        x -= self.left
        y -= self.top
        x = x // self.cell_size
        y = y // self.cell_size
        if not (0 <= x <= self.width and 0 <= y <= self.height):
            pos = None
        else:
            pos = x, y
        return pos

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.col[x][y] == (0, 0, 0):
            self.col[x][y] = (0, 255, 0)

    def get_click(self, mouse_pos):
        cell = self.get_coords(mouse_pos)
        self.on_click(cell)


class Life(Board):
    def __init__(self, *sp):
        self.sp = list(*sp)


pygame.init()
size = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра «Жизнь»')
board = Board(24, 24)
running = True
while running:
    screen.fill((0, 0, 0))
    board.render(screen)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                position = board.get_coords(event.pos)
                board.get_click(event.pos)
                board.render(screen)
                print(position)
            elif event.button == 3:
                running = False
        if keys[pygame.K_SPACE]:
            running = False
    pygame.display.flip()


