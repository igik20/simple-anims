import random
import pygame

class Chaser():
    def __init__(self) -> None:
        self.x = random.randint(0,1920)
        self.y = random.randint(0,1080)
        self.v = [0, 0]
        self.col = pygame.Color( (0,0,0) )
        self.col.hsva = (random.randint(0,360), 80, 95, 100)

    def update(self):
        mx, my = pygame.mouse.get_pos()
        self.a = [(mx - self.x) / 100, (my - self.y) / 100]
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.x += self.v[0]
        if self.x < 0:
            self.x = 0
        elif self.x > 1920:
            self.x = 1920
        self.y += self.v[1]
        if self.y < 0:
            self.y = 0
        elif self.y > 1080:
            self.y = 1080

    def draw(self):
        pygame.draw.circle(screen, self.col, (self.x, self.y), 30)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (1920, 1080) )

scrcol = pygame.Color( (0,0,0) )
scrcol.hsva = (0, 70, 100, 100)

chasers = [Chaser() for _ in range(50)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill( scrcol )
    hsva = list(scrcol.hsva)
    hsva[0] = (hsva[0] + 1) % 360
    scrcol.hsva = hsva
    for chaser in chasers:
        chaser.update()
        chaser.draw()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()