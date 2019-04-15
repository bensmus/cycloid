import pygame as pg
import math as m
pg.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# Offset
xcent = 200
ycent = 200

# Results from matrix
xvirt = 1
yvirt = 0
fps = 10

# Constant radian angle for the rotation matrix
angle = 0.02

run = True
while run:
    # Each iteration takes 1/fps seconds
    # Angular velocity is 0.02 rad / 0.1 sec
    # = 0.2 rad / sec ~ 10 deg / sec
    clock.tick(fps)
    screen.fill(WHITE)
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

########Rotation matrix#######
    # Future pos from past pos
    xvirt = xvirt * m.cos(angle) - yvirt * m.sin(angle)
    yvirt = xvirt * m.sin(angle) + yvirt * m.cos(angle)

    pg.draw.line(
        screen, BLACK,
        [xcent, ycent], [xvirt * 100 + xcent, yvirt * 100 + ycent], 3)
##############################
    pg.display.update()

pg.quit()
