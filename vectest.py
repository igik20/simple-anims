import pygame
from vec2d import Vec2D

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

ctr = Vec2D(360, 360)
v1 = Vec2D(70, 70)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( (0, 0, 0) )

    v1.rotate(0.1)

    pygame.draw.circle(screen, (255, 255, 255), (ctr + v1).c, 4)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()