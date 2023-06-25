import pygame
import sys


def terminate():  # выходим
    pygame.quit()
    sys.exit()


def load_level(filename):  # читаем текстовый файл
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def start_screen():  # заставка
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    fon = pygame.transform.scale(pygame.image.load('fon.jpg'), (500, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# загружаем картинки и спрайты
tile_images = {'wall': pygame.image.load('box.png'), 'empty': pygame.image.load('grass.png')}
player_image = pygame.image.load('mar.png')
tile_width = tile_height = 50
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
walls = []


class Tile(pygame.sprite.Sprite):  # клеточки и их содержимое
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile = tile_type
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):  # игрок и его положение
    def __init__(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def info(self):
        return self.x, self.y


def generate_level(level):  # прогружаем клетки с содержимым
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                walls.append((x, y))
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1 for j in range(height)] for i in range(width)]
        self.left = 0
        self.top = 0
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, "black", (self.left + x * self.cell_size,
                                                   self.top + y * self.cell_size,
                                                   self.cell_size,
                                                   self.cell_size), self.board[x][y])


if __name__ == '__main__':
    FPS = 50
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    start_screen()
    player, level_x, level_y = generate_level(load_level('map.txt'))

    size = width2, height2 = 550, 550
    screen2 = pygame.display.set_mode(size)
    screen2.fill((255, 255, 255))
    board = Board(11, 11)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x, y = player.info()
                    if x != 0:
                        if (x - 1, y) not in walls:
                            player.kill()
                            player = Player(x - 1, y)
                if event.key == pygame.K_RIGHT:
                    x, y = player.info()
                    if x != 11:
                        if (x + 1, y) not in walls:
                            player.kill()
                            player = Player(x + 1, y)
                if event.key == pygame.K_DOWN:
                    x, y = player.info()
                    if y != 11:
                        if (x, y + 1) not in walls:
                            player.kill()
                            player = Player(x, y + 1)
                if event.key == pygame.K_UP:
                    x, y = player.info()
                    if y != 0:
                        if (x, y - 1) not in walls:
                            player.kill()
                            player = Player(x, y - 1)
        screen2.fill((0, 0, 0))
        board.render(screen2)
        for i in all_sprites:
            screen2.blit(i.image, i.rect)
        pygame.display.flip()



