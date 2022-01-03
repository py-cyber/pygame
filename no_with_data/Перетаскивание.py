import pygame as pg


def main():
    rect_x, rect_y = 0, 0
    x = x2 = y = y2 = 0
    running = True
    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x < rect_x) or (x > rect_x + 100) or (y < rect_y) or (y > rect_y + 100):
                    x = y = 0
            if event.type == pg.MOUSEBUTTONUP:
                rect_x += x2
                rect_y += y2
                x = x2 = y = y2 = 0
            if event.type == pg.MOUSEMOTION and x > 0:
                x2 = event.pos[0] - x
                y2 = event.pos[1] - y
            pg.draw.rect(screen, 'green', ((rect_x + x2, rect_y + y2), (100, 100)))
            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    size = w, h = 300, 300
    screen = pg.display.set_mode(size)
    pg.display.set_caption('Перетаскивание')
    main()
    pg.quit()
