import pygame
import random

class Firework():
    def __init__(self, pos, v):
        self.pos = pos
        self.v = v
        self.visible = True
        self.particles = []
    
    def __update__(self):
        for i in range(len(self.pos)):
            self.pos[i] += self.v[i]
        self.v[1] += 0.01
        if self.visible and self.v[1] > 0:
            self.visible = False
            self.spawn_particles()

    def draw(self):
        if self.v[1] <= 0:
            pygame.draw.circle(screen, (255, 255, 255), self.pos, 3)

    def spawn_particles(self):
        for _ in range(30):
            p = Particle(self.pos)
            self.particles.append(p)

class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.v = [random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)]
    
    def __update__(self):
        for i in range(len(self.pos)):
            self.pos[i] += self.v[i]
        # self.v[1] += 0.01

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 3)

pygame.init()
screen = pygame.display.set_mode( (720, 720) )
clock = pygame.time.Clock()

f1 = Firework([360, 720], [0, -3])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( (0,0,0) )
    f1.__update__()
    f1.draw()
    for particle in f1.particles:
        particle.__update__()
        particle.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()