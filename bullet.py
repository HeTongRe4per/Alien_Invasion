import pygame


class Bullet:
    def __init__(self, screen, player):
        self.screen = screen
        self.image = pygame.image.load('images/bullet_p.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect.topleft)
