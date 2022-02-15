import pygame
import random
import gc

class Drop():
    def __init__(self) -> None:
        self.x = random.randint(0,720)
        self.y = 0
        self.vy = random.uniform(15,25)
        self.g = random.uniform(0.05, 0.14)
        self.a = random.choice([50, 100, 150, 200, 255])
    
    def __update__(self):
        self.y += self.vy
        self.vy += self.g

    def draw(self):
        pygame.draw.rect(s, (152, 60, 158, self.a), pygame.Rect(self.x, self.y, 3, self.a//10))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )
s = pygame.Surface( (720, 720), flags = pygame.SRCALPHA )

drops = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( (237, 135, 225) )
    s.fill( (0,0,0,0) )
    for drop in drops:
        drop.__update__()
        drop.draw()
        if drop.y > 720:
            del drop
    if random.random() > 0.3:
        drops.append(Drop())
    screen.blit(s, (0,0))
    pygame.display.flip()
    # the actual code
    clock.tick(30)

pygame.quit()