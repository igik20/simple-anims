import pygame
import random

class Drop():
    def __init__(self) -> None:
        self.x = random.randint(0,720)
        self.y = 0
        self.vy = 20
        self.s = pygame.Surface( (720, 720), flags = pygame.SRCALPHA )
    
    def __update__(self):
        self.y += self.vy
        self.vy += 0.08

    def draw(self):
        self.s.fill( (0, 0, 0, 0) )
        pygame.draw.rect(self.s, (152, 60, 158), pygame.Rect(self.x, self.y, 3, 25))
        screen.blit(self.s, (0,0))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

drops = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( (237, 135, 225) )
    if random.random() > 0.7:
        drops.append(Drop())
    for drop in drops:
        drop.__update__()
        drop.draw()
    pygame.display.flip()
    # the actual code
    clock.tick(30)

pygame.quit()