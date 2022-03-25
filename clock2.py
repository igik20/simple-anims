import pygame
from pygame import gfxdraw
import datetime
import math
from vec2d import Vec2D

def draw_arc(surface, color, center, r, start, stop, th):
    x, y = center
    points_outer = []
    points_inner = []
    n = round(r*abs(stop-start)/20)
    if n<2:
        n = 2
    for i in range(n):
        delta = i/(n-1)
        phi0 = start + (stop-start)*delta
        x0 = round(x+r*math.cos(phi0))
        y0 = round(y+r*math.sin(phi0))
        points_outer.append([x0,y0])
        phi1 = stop + (start-stop)*delta
        x1 = round(x+(r-th)*math.cos(phi1))
        y1 = round(y+(r-th)*math.sin(phi1))
        points_inner.append([x1,y1])
    points = points_outer + points_inner        
    pygame.gfxdraw.aapolygon(surface, points, color)
    pygame.gfxdraw.filled_polygon(surface, points, color)

def gradient_rect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 1,0 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 0,1 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    screen.blit( colour_rect, target_rect )                                    # paint it

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (1080, 1080) )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    T = datetime.datetime.now()

    gradient_rect(screen, (255, 135, 180), (226, 62, 87), pygame.Rect(0, 0, 1080, 1080))

    h = (T.hour % 12) / 12
    m = (T.minute % 60) / 60
    s = (T.second % 60) / 60

    draw_arc(screen, (49, 29, 63), (540, 540), 150, - math.pi / 2, 2 * math.pi * h - math.pi / 2, 20)
    draw_arc(screen, (82, 37, 70), (540, 540), 300,  - math.pi / 2, 2 * math.pi * m - math.pi / 2, 16)
    draw_arc(screen, (136, 48, 78), (540, 540), 450, - math.pi / 2, 2 * math.pi * s - math.pi / 2, 12)
    
    pygame.display.flip()
    clock.tick(1)

pygame.quit()