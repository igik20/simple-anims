import pygame
import math
import sys

class Pendulum():
    def __init__(self, x0, y0, angle = math.pi / 4, L = 200, damp = 0.995) -> None:
        self.L = L
        self.angle = angle
        self.angv = 0
        self.x0 = x0
        self.y0 = y0
        self.g = 2
        self.damp = damp

    def __update__(self):
        self.x = self.L * math.sin(self.angle) + self.x0
        self.y = self.L * math.cos(self.angle) + self.y0
        self.angv += (-1 * self.g * math.sin(self.angle)) / self.L
        self.angv *= self.damp
        self.angle += self.angv

    def draw(self):
        pygame.draw.line(screen, (255, 255, 255), (self.x0, self.y0), (self.x, self.y))
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 25)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (1000, 700) )

if len(sys.argv) < 4:
    raise SystemExit("Usage: python3 pendulum.py [angle in rad] [length] [dampening ]")

angle = float(sys.argv[1])
L = int(sys.argv[2])
damp = float(sys.argv[3])

pendulum = Pendulum(500, 0, angle, L, damp)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( (0,0,0) )
    pendulum.__update__()
    pendulum.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()