import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
mouse = pygame.image.load('creature.png')
speed = 10
x, y = 0, 0
left, right, up, down = False, False, False, False
while True:
    screen.fill((255, 255, 255))
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False
    if right:
        x += speed
    if left:
        x -= speed
    if down:
        y += speed
    if up:
        y -= speed
    screen.blit(mouse, (x, y))
    pygame.display.update()


