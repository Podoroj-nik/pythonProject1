'''import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 400, 250
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True
    k = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                h1, h2 = event.pos
                k.append([h1, h2, '-', '-'])
        if len(k) != 0:
            screen.fill((0, 0, 0))
            for el in range(len(k)):
                f = k[el]
                fx, fy = f[2], f[3]
                pygame.draw.circle(screen, (255, 255, 255), (f[0], f[1]), 10)
                if f[2] == '-':
                    g1 = int(f[0]) - 1
                else:
                    g1 = int(f[0]) + 1
                if f[3] == '-':
                    g2 = int(f[1]) - 1
                else:
                    g2 = int(f[1]) + 1
                if g1 == 10 or g1 == 390:
                    if f[2] == '-':
                        fx = '+'
                    elif f[2] == '+':
                        fx = '-'
                if g2 == 10 or g2 == 240:
                    if f[3] == '-':
                        fy = '+'
                    elif f[3] == '+':
                        fy = '-'
                k[el] = g1, g2, fx, fy
            clock.tick(100)
            pygame.display.flip()
    pygame.quit()'''


'''import random
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Я слежу за тобой!')
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    running = True
    schet = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEOEXPOSE:
                screen.fill((0, 0, 0))
                schet += 1
                print(1)
                font = pygame.font.Font(None, 100)
                text = font.render(f'{schet}', True, (255, 0, 0))
                text_x = width // 2 - text.get_width() // 2
                text_y = height // 2 - text.get_height() // 2
                screen.blit(text, (text_x, text_y))
                pygame.display.flip()
        pygame.display.flip()
    pygame.quit()'''

import pygame
import os
import sys

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('GameOver')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image



    class Car(pygame.sprite.Sprite):
        image = load_image("creature.png")

        def __init__(self, group):
            super().__init__(group)
            self.image = Car.image
            self.rect = self.image.get_rect()


        def up(self):
            self.rect = self.rect.move(0, -10)

        def doun(self):
            self.rect = self.rect.move(0, 10)

        def right(self):
            self.rect = self.rect.move(10, 0)

        def left(self):
            self.rect = self.rect.move(-10, 0)



    all_sprites = pygame.sprite.Group()
    Car(all_sprites)
    pygame.display.flip()
    running = True
    sp = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.get_pressed())
                if event.key == pygame.K_LEFT:
                    all_sprites.left()
                elif event.key == pygame.K_RIGHT:
                    all_sprites.right()
                elif event.key == pygame.K_UP:
                    all_sprites.up()
                elif event.key == pygame.K_DOWN:
                    all_sprites.down()
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()

