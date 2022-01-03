import pygame as pg


def draw(n):
    screen.fill('black')
    step = w // 2 // n
    for i in range(0, w // 2, step):
        rec_w = [(i, 0), (w - i * 2, w)]
        pg.draw.ellipse(screen, 'white', rec_w, 1)
        rec_h = [(0, i), (w, w - i * 2)]
        pg.draw.ellipse(screen, 'white', rec_h, 1)


if __name__ == '__main__':
    try:
        pg.init()
        n = int(input())
        size = w, h = 300, 300
        screen = pg.display.set_mode(size)
        draw(n)
        pg.display.set_caption('Сфера')
        while pg.event.wait().type != pg.QUIT:
            pg.display.flip()
        pg.quit()
    except Exception:
        print('Неправильный формат ввода')
        pg.quit()
