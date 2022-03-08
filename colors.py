import random
import pygame

class ColSquare():
    def __init__(self, x = 0, y = 0, r = 720) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.col = pygame.Color( (0,0,0,0) )
        self.h = random.randint(0,360)
        self.s = random.randint(40,100)
        self.v = random.randint(40,100)
        self.col.hsva = (self.h, self.s, self.v, 100)

    def update(self):
        self.h = (self.h + 1) % 360
        self.col.hsva = (self.h, self.s, self.v, 100)

    def draw(self):
        pygame.draw.rect(screen, self.col, (self.x, self.y, self.x + self.r, self.y + self.r))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

squares = [ColSquare(180 * i, 180 * j, 180) for i in range(4) for j in range(4)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for square in squares:
        square.update()
        square.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()