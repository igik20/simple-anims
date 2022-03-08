import pygame
import math

class SineObj():
    def __init__(self, x = 0, y = 360, dir = 1) -> None:
        self.x = x
        self.y = y
        self.i = 0
        self.dir = dir

    def __update__(self):
        self.vy = math.cos(self.i / 400 * 2 * math.pi) * 5
        self.y += self.vy
        self.i += 1

    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 10)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

obj = SineObj(360, 360, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( (0,0,0) )
    obj.__update__()
    obj.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()