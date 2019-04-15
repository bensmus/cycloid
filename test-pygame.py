import pygame as pg
pg.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

run = True
while run:
    screen.fill(WHITE)
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    'program'
    dt = clock.tick(10)
    print(dt)
    pg.draw.line(screen, BLACK, [0, 0], [100, 100], 10)
    'end program'

    pg.display.update()

pg.quit()
