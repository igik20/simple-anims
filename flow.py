from mimetypes import init
import pygame
import noise
import random
from math import sin, cos

class Particle():
    def __init__(self) -> None:
        self.x = random.randint(0, 720)
        self.y = random.randint(0, 720)
        self.v = [random.randint(-10,10) for i in range(2)]
        self.a = [0, 0]

    def __update__(self):
        self.x += self.v[0]
        self.y += self.v[1]
        for i in range(2):
            self.v[i] += self.a[i]
            self.v[i] = self.v[i] * 0.9
        if self.x > 720:
            self.x = 0
        elif self.x < 0:
            self.x = 720
        if self.y > 720:
            self.y = 0
        elif self.y < 0:
            self.y = 720
    
    def apply_vect(self, vect):
        for i in range(2):
            self.a[i] = vect[i]

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), (self.x, self.y), 2)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

particles = [Particle() for _ in range(100)]
field = [[noise.snoise2(3 * i, 3 * j) for i in range(73)] for j in range(73)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( pygame.Color(255, 255, 255) )
    for particle in particles:
        particle.__update__()
        n = field[int(particle.x) // 10][int(particle.y) // 10]
        v = [cos(n), sin(n)]
        particle.apply_vect(v)
        particle.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()