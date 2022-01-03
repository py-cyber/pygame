import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Я слежу за тобой!')
    running = True
    screen.fill('black')
    n = 0
    while running:
        for event in pygame.event.get():
            screen.fill('black')
            font = pygame.font.Font(None, 100)
            text = font.render(f'{n}', True, (255, 0, 0))
            textw, texth = text.get_rect().size
            screen.blit(text, [(width - textw) // 2, (height - texth) // 2])
            screen2 = pygame.Surface(screen.get_size())
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                n += 1
            pygame.display.flip()
    pygame.quit()
