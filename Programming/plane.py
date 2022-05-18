import pygame
from game.constants import Constants

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


  #  def __int__(self):
        super().__init__()
        self.frames = [
            pygame.image.load('C:/Users/15732/PycharmProjects/flappybird/tappyplane/PNG/Planes/planeBlue1.png').convert_alpha(),
            pygame.image.load('C:/Users/15732/PycharmProjects/flappybird/tappyplane/PNG/Planes/planeBlue2.png').convert_alpha(),
            pygame.image.load('C:/Users/15732/PycharmProjects/flappybird/tappyplane/PNG/Planes/planeBlue3.png').convert_alpha()
        ]
        self.frame = 0
        self.frame_count = 0
        self.image = self.frames[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.y_pos = Constants.screen_height/2
        self.rect.center = (75, self.y_pos)
        self.falling = True

    def reset(self):
        self.y_pos = Constants.screen_height / 2
        self.rect.center = (75, self.y_pos)

    def update(self):
        self.frame_count += 1
        if self.frame_count > Constants.plane_frame_rate:
            self.frame += 1
            self.frame_count = 0
        if self.frame_count >= len(self.frames):
            self.frame = 0
        self.image = self.frames[self.frame]
        self.mask = pygame.mask.from_surface(self.image)

        if self.falling:
            self.y_pos += Constants.plane_force2
        else:
            self.y_pos -= Constants.plane_force

        self.rect.center = (75, self.y_pos)

        self.falling = True

    def apply_up(self):
        self.falling = False




