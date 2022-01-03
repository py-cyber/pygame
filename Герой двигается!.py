import os
import sys

import pygame

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 15
pygame.init()
screen = pygame.display.set_mode(SIZE)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image('creature.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 10


def main():
    pygame.display.set_caption('Герой двигается!')
    running = True
    all_sprites = pygame.sprite.Group()
    hero = Hero(all_sprites)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            hero.update()
        screen.fill('white')
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
    pygame.display.quit()


if __name__ == '__main__':
    main()
