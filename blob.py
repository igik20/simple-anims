import pygame
from noise import pnoise1

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (720, 720) )

layers = [pygame.Surface((720, 720), pygame.SRCALPHA) for _ in range(2)]

BGCOLOR = (240, 233, 233, 255)
BLOBCOLORS = ( pygame.Color((193, 145, 145, 60)), pygame.Color((170, 112, 112, 130)), pygame.Color((139, 93, 93, 240)) )

cnt = pygame.Vector2(360, 360)
frame_count = 0

running = True
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # clear the screen every frame
    screen.fill(BGCOLOR)
    for layer in layers:
        layer.fill( (0, 0, 0, 0) )

    # generating the blobs
    coords = []
    for i, layer in enumerate(layers):
        for angle in range(360):
            coord = pygame.Vector2()
            n1 = pnoise1(angle / 36 + 0.1)
            n2 = pnoise1(angle / 120 + frame_count / 100 + i)
            coord.from_polar( (240 - 80 * i + (100 - 20 * i) * n1 + (100 - 20 * i) * n2, angle) )
            coord += cnt
            coords.append(coord)
        pygame.draw.polygon(layer, BLOBCOLORS[i], coords)
        screen.blit(layer, (0, 0), special_flags = pygame.BLEND_ALPHA_SDL2)
    
    pygame.display.flip()
    # frame_count += 1
    clock.tick(30)

pygame.quit()