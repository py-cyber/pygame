import pygame

size = width, height = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Прямоугольники с Ctrl+Z')
x1, y1, w, h = 0, 0, 0, 0
drawing = False
running = True
start_x = []
start_y = []
rect_width = []
rect_height = []
while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if event.mod & pygame.KMOD_LCTRL or event.mod & pygame.KMOD_RCTRL:
                    start_x.pop()
                    start_y.pop()
                    rect_width.pop()
                    rect_height.pop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
            w, h = x1, y1
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            start_x.append(x1)
            start_y.append(y1)
            rect_width.append(w - x1)
            rect_height.append(h - y1)
        if event.type == pygame.MOUSEMOTION:
            w, h = event.pos
    for i in range(len(start_x)):
        pygame.draw.rect(screen, 'white', ((start_x[i], start_y[i]), (rect_width[i], rect_height[i])), 5)
    if drawing:
        pygame.draw.rect(screen, 'white', ((x1, y1), (w - x1, h - y1)), 5)
    pygame.display.flip()
pygame.quit()
