import pygame as pg
import math as m
pg.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pg.display.set_mode((1000, 600))
clock = pg.time.Clock()

def fadeYellowToBlack(i):
    # Will be returning (r, g, b) values depending on index
    # We want a fade of:
    '''(0, 0, 0) -> (255, 0, 0) -> (255, 255, 0) -> (255, 255, 255)
           0              700            1400            2100'''
    # Newest points are first, and will always be black
    # Assume that the maximum index is 2100
    r = g = b = 0
    if i <= 700:
        r = i / 700 * 255
    elif i <= 1400:
        r = 255
        g = (i - 700) / 700 * 255
    else:
        r = 255
        g = 255
        b = (i - 1400) / 700 * 255
    return r, g, b

# Offset
xcent = 100
ycent = 100

# Results from matrix
x = 100
y = 0
fps = 50

# Constant radian angle for the rotation matrix
angle = 0.02

# Horizontal translation value in px
shift = 0.3

# Storing all of the points on the tip of the
# Rotating and translating line
tailpoints = []

run = True
while run:
    # Each iteration takes 1/fps sec
    # Angular velocity is 0.02 rad / 0.02 sec
    # = 1 rad / sec ~ 57.3 deg / sec
    # Translational velocity is 0.3 px / 0.1 sec
    # = 3 px / sec

    clock.tick(fps)
    screen.fill(WHITE)
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if len(tailpoints) == 2100:
        run = False

    # Shifting of center
    xcent += shift

    # Rotation matrix
    # Future pos from past pos
    x = x * m.cos(angle) - y * m.sin(angle)
    y = x * m.sin(angle) + y * m.cos(angle)

    # Drawing line
    pg.draw.line(screen, BLACK,
        [xcent, ycent], [x + xcent, y + ycent], 3)

    # Updating and drawing tailpoints
    tailpoints.append([x + xcent, y + ycent])

    for i, tailpoint in enumerate(tailpoints[::-1]):
        pg.draw.line(screen, fadeYellowToBlack(i), tailpoint, tailpoint, 3)

    pg.display.update()

pg.quit()
