import pygame

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 15


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.display.quit()


if __name__ == '__main__':
    main()
