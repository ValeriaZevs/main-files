import pygame
import sys


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 400 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 400 // 2)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Финал", "",
                  "",
                  "Цикл игры"]

    fon = pygame.transform.scale(pygame.image.load('fon.jpg'), (500, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
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
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player = None
    for y in range(-len(level), 2 * len(level)):
        yn = y
        if yn >= len(level):
            yn %= len(level)
        for x in range(-len(level[yn]), 2 * len(level[yn])):
            xn = x
            if xn >= len(level[yn]):
                xn %= len(level[yn])
            if level[yn][xn] == '.':
                Tile('empty', x, y)
            elif level[yn][xn] == '#':
                Tile('wall', x, y)
            elif level[yn][xn] == '@':
                Tile('empty', xn, yn)
                new_player = Player(xn, yn)
    return new_player

pygame.init()
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Финал")
FPS = 50
tile_images = {'wall': pygame.image.load('box.png'), 'empty': pygame.image.load('grass.png')}
player_image = pygame.image.load('mar.png')
tile_width = tile_height = 50
#//////////////////////////////////////////////////////////////////////////////////////////////
player = None
running = True
clock = pygame.time.Clock()
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
#//////////////////////////////////////////////////////////////////////////////////////////////
start_screen()
camera = Camera()
level_map = load_level('map.txt')
for i in range(len(level_map)):
    if "@" in level_map[i]:
        y, x = i, level_map[i].find("@")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if y < 10 and level_map[y + 1][x] == ".":
                    level_map[y] = level_map[y][:x] + "." + level_map[y][x + 1:]
                    level_map[y + 1] = level_map[y + 1][:x] + "@" + level_map[y + 1][x + 1:]
                    y += 1
                elif y >= 10 and level_map[y - 10][x] == ".":
                    level_map[y] = level_map[y][:x] + "." + level_map[y][x + 1:]
                    level_map[0] = level_map[0][:x] + "@" + level_map[0][x + 1:]
                    y = 0
            if event.key == pygame.K_LEFT:
                if x > 0 and level_map[y][x - 1] == ".":
                    level_map[y] = level_map[y][:x - 1] + "@." + level_map[y][x + 1:]
                    x -= 1
                elif x <= 0 and level_map[y][-1] == ".":
                    level_map[y] = "." + level_map[y][1:-1] + "@"
                    x = 10
            if event.key == pygame.K_RIGHT:
                if x < 10 and level_map[y][x + 1] == ".":
                    level_map[y] = level_map[y][:x] + ".@" + level_map[y][x + 2:]
                    x += 1
                elif x >= 10 and level_map[y][0] == ".":
                    level_map[y] = "@" + level_map[y][:-2] + "."
                    x = 0
            if event.key == pygame.K_UP:
                if y > 0 and level_map[y - 1][x] == ".":
                    level_map[y] = level_map[y][:x] + "." + level_map[y][x + 1:]
                    level_map[y - 1] = level_map[y - 1][:x] + "@" + level_map[y - 1][x + 1:]
                    y -= 1
                elif y <= 0 and level_map[-1][x] == ".":
                    level_map[0] = level_map[0][:x] + "." + level_map[0][x + 1:]
                    level_map[-1] = level_map[-1][:x] + "@" + level_map[-1][x + 1:]
                    y = 10
    screen.fill((0, 0, 0))
    clock.tick(FPS)
    player = generate_level(level_map)
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.update(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
