import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # the actual code
    pygame.display.flip()
    clock.tick(30)

pygame.quit()