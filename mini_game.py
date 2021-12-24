from random import randint

import pygame
import pickle


SIZE = WIDTH, HEIGHT = 800, 600
TIMER_EVENT_TYPE = 30
DATA_DIR = 'data'

class ClickMe:
    def __init__(self):
        self.width = 200
        self.height = 60
        self.x = randint(0, WIDTH - self.width)
        self.y = randint(0, HEIGHT - self.height)
        self.delay = 1000
        pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)
        self.score = 0
        self.bed_score = 0
        self.stop = False
        self.lose = False

    def render(self, screen):
        font = pygame.font.Font(None, 50)
        text = font.render('Click me!', 1, (50, 70, 0))
        pygame.draw.rect(screen, (200, 50, 70), (self.x, self.y, self.width, self.height), 0)
        screen.blit(text, (self.x + (self.width - text.get_width()) // 2,
                           self.y + (self.height - text.get_height()) // 2))

        font = pygame.font.Font(None, 25)
        text = font.render(f'your score: {self.score}, your miss: {self.bed_score}', 1, (200, 166, 244))
        screen.blit(text, (10, 10))

        if self.lose:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 100)
            text = font.render('u lose(', 1, (255, 0, 0))
            screen.blit(text, (250, 250))
            pygame.time.set_timer(TIMER_EVENT_TYPE, 0)
            pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)

    def move(self):
        self.x = randint(0, WIDTH - self.width)
        self.y = randint(0, HEIGHT - self.height)

    def check_click(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.move()
            self.delay = max(self.delay - 50, 50)
            pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay)
            self.score += 1
        else:
            self.bed_score += 1
            if self.bed_score == 30:
                self.lose = True


    def switch_stop(self):
        self.stop = not self.stop
        pygame.time.set_timer(TIMER_EVENT_TYPE, self.delay if not self.stop else 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    clm = ClickMe()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == TIMER_EVENT_TYPE:
                clm.move()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clm.check_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    clm.switch_stop()
                if event.key == pygame.K_s:
                    with open(f'{DATA_DIR}/save.dat', 'wb') as file:
                        pickle.dump(clm, file)
                if event.key == pygame.K_l:
                    with open(f'{DATA_DIR}/save.dat', 'rb') as file:
                        clm = pickle.load(file)
        screen.fill((0, 0, 0))
        clm.render(screen)
        pygame.display.flip()
    pygame.display.quit()


if __name__ == '__main__':
    main()
