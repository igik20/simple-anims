import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    T = datetime.datetime.now()
    screen.fill( (0, 0, 0) )
    h = (T.hour % 12) / 12
    col_h = pygame.Color( (0, 0, 0) )
    col_h.hsva = (180 - h * 180, 70, 100, 100)
    w_h = h * 720
    pygame.draw.rect(screen, col_h, (0, 0, w_h, 240))
    m = (T.minute % 60) / 60
    col_m = pygame.Color( (0, 0, 0) )
    col_m.hsva = (180 - m * 180, 70, 100, 100)
    w_m = m * 720
    pygame.draw.rect(screen, col_m, (0, 240, w_m, 240))
    s = (T.second % 60) / 60
    col_s = pygame.Color( (0, 0, 0) )
    col_s.hsva = (180 - s * 180, 70, 100, 100)
    w_s = s * 720
    pygame.draw.rect(screen, col_s, (0, 480, w_s, 240))
    pygame.display.flip()
    clock.tick(3)

pygame.quit()