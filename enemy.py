import pygame
import random
from settings import *
from enemy_bullet import EnemyBullet

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = 0
        self.speed = enemy_speed
        self.can_fire = random.random() < 1/3  # 1/3 的概率设置为可以发射子弹的状态
        self.fire_delay = 50  # 发射子弹的间隔帧数
        self.fire_counter = 0  # 计数器，用于跟踪发射子弹的时间间隔

    def update(self):
        self.rect.y += self.speed
        # 更新计数器
        self.fire_counter += 1

    def fire(self, enemy_bullets):
        if self.can_fire and self.fire_counter >= self.fire_delay:
            enemy_bullets.append(EnemyBullet(self.screen, self))
            self.fire_counter = 0  # 重置计数器，重新开始计时

    def blitme(self):
        self.screen.blit(self.image, self.rect.topleft)
