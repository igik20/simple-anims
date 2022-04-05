from math import ceil
import pygame

BGCOLOR = pygame.Color(229, 239, 193)
BGCOLOR2 = pygame.Color(0, 0, 0)
LINECOLOR = pygame.Color(57, 174, 169)
TRUECOLOR = pygame.Color(255, 255, 255)

class FadeLine():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.a = 100
        self.col = LINECOLOR

    def update(self):
        if self.a > 1:
            self.a -= 0.5
        h, s, v = self.col.hsva[0:3]
        self.col.hsva = (h, s, v, ceil(self.a))

    def draw(self):
        pygame.draw.line(s, self.col, (self.x0, self.y0), (self.x1, self.y1), 10)

class TrueLine():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.col = TRUECOLOR

    def draw(self):
        pygame.draw.line(s, self.col, (self.x0, self.y0), (self.x1, self.y1), 10)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (1080, 1080) )
s = pygame.Surface( (1080, 1080), pygame.SRCALPHA )

fadelines = []
truelines = []
mousedown = False
prev = (0, 0)
view = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
            prev = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                view = not view
    
    if mousedown and not view:
        x, y = pygame.mouse.get_pos()
        fadelines.append(FadeLine(prev[0], prev[1], x, y))
        truelines.append(TrueLine(prev[0], prev[1], x, y))
        prev = (x, y)
    
    if not view:
        screen.fill(BGCOLOR)
        s.fill( (0,0,0,0) )
    else:
        screen.fill(BGCOLOR2)
        s.fill( (0,0,0,0) )

    if not view:
        for fl in fadelines:
            fl.update()
            fl.draw()
            if fl.col.hsva[3] <= 1:
                del fl
    else:
        for tl in truelines:
            tl.draw()

    screen.blit(s, (0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()