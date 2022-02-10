import pygame
import random

class Circle():
    def __init__(self):
        self.x = random.randint(0, 720)
        self.y = random.randint(0, 720)
        self.r = 1
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        self.color = pygame.Color(red, green, blue, 255)
        self.s = pygame.Surface( (720, 720), flags = pygame.SRCALPHA )

    def __update__(self):
        self.r += 1
        if random.randint(0,1) == 1:
            self.color.a = self.color.a - 1 if self.color.a > 0 else 0

    def draw(self):
        self.s.fill( (0, 0, 0, 0) )
        pygame.draw.circle(self.s, self.color, (self.x, self.y), self.r, 2)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if random.randint(1,100) > 98:
        circles.append(Circle())
    screen.fill( (0, 0, 0) )
    for circle in circles:
        circle.__update__()
        circle.draw()
        screen.blit(circle.s, (0, 0) )
    pygame.display.flip()
    clock.tick(30)

pygame.quit()