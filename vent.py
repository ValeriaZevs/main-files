import pygame
import math


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([201, 201])
    screen.fill(pygame.Color('black'))
    clock = pygame.time.Clock()
    running = True
    fps = 10

    transform, rotation, center_radius, a, b = 0, 0, 10.0, 70, 70
    angle = 0.5235987755982988
    base = math.sqrt((a ** 2 + b ** 2) - (2 * a * b * math.cos(angle)))
    coords = [[(101, 101), (101 + base / 2, 101 - a), (101 - base / 2, 101 - a)],
              [(101, 101), (171, 121), ((101 + base / 2) + 35, 150)],
              [(101, 101), (101 - 70, 121), ((101 - base / 2) - 35, 150)]]

    screen2 = pygame.Surface((201, 201), pygame.SRCALPHA)
    pygame.draw.circle(screen2, pygame.Color('WHITE'), (101, 101), center_radius)
    pygame.draw.polygon(screen2, pygame.Color('WHITE'), coords[0])
    pygame.draw.polygon(screen2, pygame.Color('WHITE'), coords[1])
    pygame.draw.polygon(screen2, pygame.Color('WHITE'), coords[2])
    screen.blit(screen2, (0, 0))

    while running:
        screen.fill(pygame.Color('BLACK'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    transform -= 10
                if event.button == 3:
                    transform += 10
        rotation += transform
        screen3 = pygame.transform.rotate(screen2, rotation)
        rect = screen3.get_rect()
        rect.center = (101, 101)
        screen.blit(screen3, rect)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()