import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Жёлтый круг')
    pygame.time.set_timer(pygame.USEREVENT, 10)
    circle, running, radius = False, True, 20
    screen.fill('blue')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                circle, radius, circle_pos = True, 20, event.pos
                screen.fill('blue')
                pygame.draw.circle(screen, 'yellow', circle_pos, radius)
            if event.type == pygame.USEREVENT and circle:
                pygame.draw.circle(screen, 'yellow', circle_pos, radius)
                radius += 1
        pygame.display.flip()
    pygame.quit()
