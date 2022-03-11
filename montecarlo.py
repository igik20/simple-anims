import math
import random
from collections import deque
import pygame

class Point():
    def __init__(self) -> None:
        self.x = random.randint(0,720)
        self.y = random.randint(0,720)
        self.valid = (self.x - 360) ** 2 + (self.y - 360) ** 2 < 360 ** 2
        self.col = pygame.Color(51, 217, 46) if self.valid else pygame.Color(237, 62, 50)

    def draw(self):
        pygame.draw.circle(screen, self.col, (self.x, self.y), 2)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 920) )
points = []

ests = deque([(0,0) for _ in range(720)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # math section
    points.append(Point())
    valid_pts = [p for p in points if p.valid]
    pi = 4 * (len(valid_pts) / len(points))
    delta = pi - math.pi

    ests.rotate(-1)
    ests[-1] = (pi, math.pi)
    screen.fill( (0, 0, 0) )
    pygame.draw.circle(screen, (255, 255, 255), (360, 360), 360, 2)
    pygame.draw.rect(screen, (255, 255, 255), (0, 720, 720, 2))
    for point in points:
        point.draw()
    for i, est in enumerate(ests):
        e = est[0]
        ce = 720 + 200 - (200 * (e - 2.64)) if e > 0 else 1000
        t = est[1]
        te = 720 + 200 - (200 * (t - 2.64)) if t > 0 else 1000
        c = pygame.Color( (0, 0, 0) )
        d = abs(e - t)
        if 0 < d < 1:
            h = 180 * d
            c.hsva = (h, 90, 100, 100)
        if ce > 720:
            pygame.draw.circle(screen, c, (i, ce), 2)
        pygame.draw.rect(screen, (77, 235, 240), (i, te, 2, 2))
    font1 = pygame.font.SysFont("Arial", 20)
    caption1 = font1.render("Est: " + str(round(pi, 5)), True, (150, 150, 150))
    screen.blit(caption1, (2, 2))
    caption2 = font1.render("Delta: " + str(round(delta, 5)), True, (150, 150, 150))
    screen.blit(caption2, (2, 27))
    font2 = pygame.font.SysFont("Arial", 15)
    caption3 = font2.render("3.64", True, (150, 150, 150))
    screen.blit(caption3, (2, 724))
    caption4 = font2.render("2.64", True, (150, 150, 150))
    screen.blit(caption4, (2, 902))
    caption5 = font2.render("PI", True, (150, 150, 150))
    screen.blit(caption5, (2, 813))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()