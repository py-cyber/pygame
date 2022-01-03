import os
import random

import pygame
import sys

pygame.init()
SIZE = W, H = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")
    image_rotate = pygame.transform.flip(image, True, False)

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 5

    def update(self):
        if self.rect.x + self.rect.width >= W or self.rect.x <= 0:
            self.speed = -self.speed
            if self.speed > 0:
                self.image = Car.image
            else:
                self.image = Car.image_rotate
        self.rect.x += self.speed


def main():
    pygame.display.set_caption('Машинка')
    all_sprites = pygame.sprite.Group()
    Car(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        pygame.time.Clock().tick(50)
    pygame.quit()


if __name__ == '__main__':
    main()
