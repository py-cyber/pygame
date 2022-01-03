import os
import sys
import pygame

SIZE = WIDTH, HEIGHT = 800, 600
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

class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow.png")
    def __init__(self, group):
        super().__init__(group)
        self.image = Arrow.image
        self.rect = self.image.get_rect()

    def render(self, pos):
        self.rect.topleft = pos



def main():
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Свой курсор мыши')
    all_sprites = pygame.sprite.Group()
    arr = Arrow(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                arr.render(event.pos)
        screen.fill("black")
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
