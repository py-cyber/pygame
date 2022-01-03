import pygame

if __name__ == '__main__':
    size = width, height = 400, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шарики')
    running, radius, circle_pos, speed_circle = True, 10, [], []
    screen.fill('black')
    screen2 = pygame.Surface(screen.get_size())
    while running:
        for event in pygame.event.get():
            screen2 = pygame.Surface(screen.get_size())
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                circle_pos.append(list(event.pos))
                speed_circle.append([-1, -1])
        screen2.fill(pygame.Color('black'))
        for i in range(len(circle_pos)):
            for j in range(2):
                if circle_pos[i][j] >= size[j] - radius or circle_pos[i][j] <= radius:
                    speed_circle[i][j] = -speed_circle[i][j]
                circle_pos[i][j] += speed_circle[i][j]
            pygame.draw.circle(screen2, 'white', circle_pos[i], radius)
        screen.blit(screen2, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(100)
    pygame.quit()
