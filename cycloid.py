import pygame as pg
import math as m
pg.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pg.display.set_mode((1000, 600))
clock = pg.time.Clock()

# Offset
xcent = 100
ycent = 100

# Results from matrix
x = 100
y = 0
fps = 60

# Constant radian angle for the rotation matrix
angle = 0.02

# Horizontal translation value in px
shift = 0.2

# Storing all of the points on the tip of the
# Rotating and translating line
tailpoints = []

run = True
while run:
    # Each iteration takes 1/fps sec
    # Angular velocity is 0.02 rad / 0.1 sec
    # = 0.2 rad / sec ~ 10 deg / sec
    # Translational velocity is 1 px / 0.1 sec
    # = 10 px / sec
    clock.tick(fps)
    screen.fill(WHITE)
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.QUIT:
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

    for tailpoint in tailpoints:
        pg.draw.line(screen, BLACK, tailpoint, tailpoint)

    pg.display.update()

pg.quit()
