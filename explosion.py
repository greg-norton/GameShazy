import pygame
from library import *

class ExplosionSprite(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        super().__init__()
        self.image, self.rect = load_image('resources/misc_sprites/explosion1.png')
        self.rect = pygame.Rect(startx,starty,30,30)
        self.sound = load_sound('explosion.ogg')
        self.frame_counter = 45
        self.visible = 1

    def update(self):
        if self.frame_counter == 0:
            self.visible = 0
        self.frame_counter -= 1
        self.move(0,5)

    def move(self, diffx, diffy):
        self.rect = self.rect.move(diffx, diffy)

    def play_sound(self):
        self.sound.play()