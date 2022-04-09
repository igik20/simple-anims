from collections import deque
import pygame

import random

class PARAMS():
    # dimensions
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 1280
    
    FPS = 30

    TICKSPEED = 1
    # colors
    BG_COLOR = pygame.Color(51, 60, 131)
    PT_COLORS = [pygame.Color(253, 175, 117), pygame.Color(242, 74, 114), pygame.Color(234, 234, 127), pygame.Color(78, 162, 245)]
    # simulation parameters
    POP = 200
    INF_RATE = 0.02
    REC_RATE = 0.05
    WEAR_RATE = 0.01
    VAC_RATE = 0
    VAC_WEAR_RATE = 0.003

class Person():
    def __init__(self) -> None:
        self.x = random.randint(0, PARAMS.SCREEN_WIDTH)
        self.y = random.randint(0, PARAMS.SCREEN_HEIGHT - 205)
        self.status = 0 if random.random() > PARAMS.INF_RATE else 1
        
    def update(self):
        if self.status == 0:
            r = random.random()
            if r < PARAMS.INF_RATE:
                self.status = 1
            elif r > (1 - PARAMS.VAC_RATE):
                self.status = 3
        elif self.status == 1 and random.random() < PARAMS.REC_RATE:
            self.status = 2
        elif self.status == 2:
            r = random.random()
            if r < PARAMS.WEAR_RATE:
                self.status = 1
            elif r > (1 - PARAMS.VAC_RATE):
                self.status = 3
        elif self.status == 3 and random.random() < PARAMS.VAC_WEAR_RATE:
            self.status = 0


    def draw(self):
        pygame.draw.circle(screen, PARAMS.PT_COLORS[self.status], (self.x, self.y), 5)

screen = pygame.display.set_mode( (PARAMS.SCREEN_WIDTH, PARAMS.SCREEN_HEIGHT) )

clock = pygame.time.Clock()
framecount = 0

people = [Person() for _ in range(PARAMS.POP)]

inf_prob = 0

hist = deque([[0, 0, 0, 0] for i in range(108)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if framecount % (PARAMS.FPS / PARAMS.TICKSPEED) == 0:
        pop_stat = [0, 0, 0, 0]
        for person in people:
            person.update()
            pop_stat[person.status] += 1
        hist.append(pop_stat)
        hist.popleft()
        print(hist[-1])
        inf_prob = PARAMS.INF_RATE * pop_stat[0] * pop_stat[1] / PARAMS.POP

    screen.fill(PARAMS.BG_COLOR)

    pygame.draw.rect(screen, (0, 0, 0), (0, 1078, 1080, 2))

    for person in people:
        person.draw()

    for i, stat in enumerate(hist):
        sus = stat[0]
        inf = stat[1]
        rec = stat[2]
        vac = stat[3]
        x = 10 * i
        pygame.draw.rect(screen, PARAMS.PT_COLORS[3], (x, 1080, 10, vac))
        pygame.draw.rect(screen, PARAMS.PT_COLORS[2], (x, 1080 + vac, 10, rec))
        pygame.draw.rect(screen, PARAMS.PT_COLORS[1], (x, 1080 + vac + rec, 10, inf))
        pygame.draw.rect(screen, PARAMS.PT_COLORS[0], (x, 1080 + vac + rec + inf, 10, sus))

    pygame.display.flip()
    
    framecount += 1
    clock.tick(PARAMS.FPS)

pygame.quit()