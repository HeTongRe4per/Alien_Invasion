import pygame


class EnemyBullet:
    def __init__(self, screen, enemy):
        self.screen = screen
        self.image = pygame.image.load('images/bullet_a.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx
        self.rect.top = enemy.rect.bottom
        self.speed = 5

    def update(self):
        self.rect.y += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect.topleft)
