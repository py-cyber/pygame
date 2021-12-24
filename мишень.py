import pygame as pg


def draw(w, n):
    ncopy = n
    screen.fill('black')
    while ncopy > 0:
        pg.draw.circle(screen, palette[ncopy % 3], (w * n, w * n), w * ncopy)
        ncopy -= 1


if __name__ == '__main__':
    try:
        pg.init()
        w, n = [int(i) for i in input().split()]
        size = w * 2 * n, w * 2 * n
        palette = {0: 'blue', 1: 'red', 2: 'green'}
        screen = pg.display.set_mode(size)
        draw(w, n)
        pg.display.set_caption('Мишень')
        while pg.event.wait().type != pg.QUIT:
            pg.display.flip()
        pg.quit()
    except Exception:
        print('Неправильный формат ввода')
        pg.quit()
