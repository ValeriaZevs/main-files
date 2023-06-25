import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(400)
        self.rect.y = random.randrange(400)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = pygame.image.load("boom.png")



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boom them all")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for i in range(20):
    player = Bomb()
    all_sprites.add(player)


running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

