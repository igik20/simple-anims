import random
import pygame

class GrowBall():
    def __init__(self, x, y, r, run = False) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.run = run
        self.col = pygame.Color( (255, 255, 255) )

    def update(self):
        if self.run:
            self.r += 2

    def draw(self):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.r)

class FallBall():
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.vy = 5
        self.g = 0.5
        self.col = pygame.Color( (0, 0, 0) )
        self.col.hsva = (random.randint(0,360), 40, 90)

    def update(self):
        self.y += self.vy
        self.vy += self.g
        if self.y > 720 - self.r:
            self.y = 720 - self.r

    def draw(self):
        pygame.draw.circle(screen, self.col, (self.x, self.y), self.r)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

grow_circ = GrowBall(0, 0, 0)
fall_circs = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grow_circ.x = x
            grow_circ.y = y
            grow_circ.r = 1
            grow_circ.run = True
        elif event.type == pygame.MOUSEBUTTONUP:
            fall_circs.append(FallBall(grow_circ.x, grow_circ.y, grow_circ.r))
            grow_circ.r = 0
            grow_circ.run = False

    screen.fill( (0, 0, 0) )
    
    for circ in fall_circs:
        circ.update()
        circ.draw()

    grow_circ.update()
    grow_circ.draw()

    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()